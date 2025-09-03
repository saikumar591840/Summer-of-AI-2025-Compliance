# Deployment

## Local
- Run FastAPI on port 8000; serve client via simple HTTP server.
- Set CORS to allow your client origin.

## Cloud (Example)
- **Backend**: Deploy to Render/Fly.io/Heroku.
- **DB**: Use managed Postgres; update SQLAlchemy URL.
- **Frontend**: Netlify/Vercel or GitHub Pages (adjust API URL).

## Environment
Create `.env` from `.env.example` and set `DATABASE_URL` and `ALLOWED_ORIGINS`.
