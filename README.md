# BALKANAPI
![Hero image](/assets/hero.png)

This is a little FastAPI app that serves funny Balkan-style quotes. It was built for the RASPAPI project and is meant to be easy to run, poke, and share.

## What it does

It gives you a few simple endpoints for getting random quotes, browsing all quotes, searching by author/category, and adding your own.

### Available endpoints

- `GET /` — quick health check
- `GET /quote` — random Balkan quote
- `GET /quotes` — all quotes
- `GET /quote/{quote_id}` — one quote by ID
- `GET /categories` — list of available categories
- `GET /search?category={category}&author={author}` — search by category or author
- `POST /quote` — add a new quote

## Docs

There is a live, interactive docs page at `/docs` once the app is running.

Try it locally at:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

Or at the vercel domain:

- `https://balkanraspapi.vercel.app/docs`
- `https://balkanraspapi.vercel.app/redoc1`
## Example POST

Here’s how to add a new quote with `curl`:

```powershell
curl -X POST "http://127.0.0.1:8000/quote" -H "Content-Type: application/json" -d "{
  \"text\": \"The only thing stronger than Balkan coffee is Balkan gossip.\",
  \"author\": \"Anonymous Auntie\",
  \"category\": \"humor\"
}"
```

## Run locally

1. Make a venv:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install the packages:

```powershell
pip install -r requirements.txt
```

3. Start the API:

```powershell
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

4. Open the docs in your browser:

```text
http://127.0.0.1:8000/docs
```

## Deploy to Vercel

If you want a public URL, deploy this repo to Vercel.

1. Push the project to GitHub.
2. Go to [vercel.com](https://vercel.com) and create a new project.
3. Pick this repo and deploy.
4. Your app should be live at something like `https://your-project-name.vercel.app`.

Then try:

```bash
curl https://your-project-name.vercel.app/docs
curl https://your-project-name.vercel.app/quote
```

## Notes

This project is supposed to be playful and easy to use. If you want, you can add more quotes, make the search smarter, or let people submit quotes from a web form.
