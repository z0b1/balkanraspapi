# RASPAPI
![Hero image](https://github.com/iiiypuk/rpi-icon/blob/master/512.png)
A simple Python FastAPI service that returns Balkan-style humorous quotes.

## Endpoints

- `GET /` — service health check
- `GET /quote` — returns a random funny Balkan quote
- `GET /quotes` — returns the full list of quotes
- `GET /quote/{quote_id}` — returns a quote by ID
- `GET /categories` — returns available quote categories
- `GET /search?category={category}&author={author}` — search quotes by category or author
- `POST /quote` — add a new quote

## OpenAPI docs

The interactive docs are available at:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## Sample POST request

```powershell
curl -X POST "http://127.0.0.1:8000/quote" -H "Content-Type: application/json" -d "{
  \"text\": \"The only thing stronger than Balkan coffee is Balkan gossip.\",
  \"author\": \"Anonymous Auntie\",
  \"category\": \"humor\"
}"
```

## Run locally

1. Create a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Start the app:

```powershell
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

4. Open `http://127.0.0.1:8000/docs` in a browser.

## Deploy to Vercel

1. Push your code to a GitHub repo (public or private).

2. Go to [vercel.com](https://vercel.com) and sign up / log in.

3. Click **"New Project"** and select your GitHub repo.

4. Vercel auto-detects Python; confirm settings and click **"Deploy"**.

5. Once deployed, your API will be live at `https://your-project-name.vercel.app`.

6. Test with:

```bash
curl https://your-project-name.vercel.app/docs
curl https://your-project-name.vercel.app/quote
```

> **Note:** The `vercel.json` file in this repo configures Vercel to run FastAPI correctly. No additional setup needed.

## Notes

This project is intentionally light and fun. Add more quotes or new endpoints for categories, search, or quote submission as needed.
