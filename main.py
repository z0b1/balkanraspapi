import logging
import random
from typing import List

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from quotes import Quote, QUOTES

logger = logging.getLogger("raspapi")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

app = FastAPI(
    title="RASPAPI",
    description="A fun Balkan-style quote API that returns classic sarcastic and humorous sayings.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.warning("HTTP error %s on %s %s", exc.status_code, request.method, request.url)
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "message": exc.detail,
            "method": request.method,
            "path": request.url.path,
        },
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning("Validation error on %s %s: %s", request.method, request.url, exc.errors())
    return JSONResponse(
        status_code=422,
        content={
            "status": "invalid_request",
            "message": "Request validation failed",
            "errors": exc.errors(),
            "method": request.method,
            "path": request.url.path,
        },
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception on %s %s", request.method, request.url)
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "Internal server error",
            "method": request.method,
            "path": request.url.path,
        },
    )

class QuoteResponse(BaseModel):
    quote: Quote
    source: str

class QuoteCreate(BaseModel):
    text: str = Field(..., example="There is no Wi-Fi in the forest, but I promise you'll find a better connection.")
    author: str = Field(..., example="Balkan Traveler")
    category: str = Field(..., example="humor")

@app.get("/", tags=["Health"])
def root() -> dict:
    return {"status": "ok", "service": "RASPAPI", "message": "Balkan humor ready."}

@app.get("/quote", response_model=QuoteResponse, tags=["Quotes"])
def get_random_quote() -> QuoteResponse:
    quote = random.choice(QUOTES)
    return QuoteResponse(quote=quote, source="random")

@app.get("/quote/{quote_id}", response_model=QuoteResponse, tags=["Quotes"])
def get_quote_by_id(quote_id: int) -> QuoteResponse:
    if quote_id < 1 or quote_id > len(QUOTES):
        raise HTTPException(status_code=404, detail="Quote not found")
    return QuoteResponse(quote=QUOTES[quote_id - 1], source="id")

@app.get("/quotes", response_model=List[Quote], tags=["Quotes"])
def list_quotes() -> List[Quote]:
    if not QUOTES:
        raise HTTPException(status_code=404, detail="No quotes available")
    return QUOTES

@app.get("/categories", response_model=List[str], tags=["Quotes"])
def list_categories() -> List[str]:
    return sorted({quote.category for quote in QUOTES})

@app.get("/search", response_model=List[Quote], tags=["Quotes"])
def search_quotes(
    category: str | None = Query(None, description="Filter quotes by category"),
    author: str | None = Query(None, description="Search quotes by author name."),
) -> List[Quote]:
    if not category and not author:
        raise HTTPException(status_code=400, detail="At least one search parameter is required")

    results = QUOTES
    if category:
        results = [quote for quote in results if quote.category.lower() == category.lower()]
    if author:
        results = [quote for quote in results if author.lower() in quote.author.lower()]

    if not results:
        raise HTTPException(status_code=404, detail="No quotes matched the search criteria")
    return results

@app.post("/quote", response_model=QuoteResponse, status_code=201, tags=["Quotes"])
def create_quote(quote_create: QuoteCreate) -> QuoteResponse:
    quote_id = max((quote.id for quote in QUOTES), default=0) + 1
    quote = Quote(id=quote_id, **quote_create.model_dump())
    QUOTES.append(quote)
    return QuoteResponse(quote=quote, source="created")
