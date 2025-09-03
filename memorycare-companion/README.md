# AI MemoryCare Companion

An innovative, socially impactful project for **Summer of AI 2025** — an empathetic AI assistant to support early dementia & elderly care.  
This monorepo includes:
- **AI Chat Assistant (server)** with FastAPI
- **Client Application (web)** with vanilla JS
- **Corpus Contribution** (unique, curated JSONL datasets)
- **Compliance Checker** script to self-verify requirements

## Quick Start

### 1) Backend (FastAPI)
```bash
cd server
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

### 2) Frontend (static web)
Open `client/index.html` in a local http server:
```bash
cd client
python -m http.server 5173
# Visit http://localhost:5173
```

### 3) Compliance Check (local)
```bash
python tools/compliance_check.py
```

### 4) Tests
```bash
cd tests
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Project Structure
```
memorycare-companion/
├── README.md
├── LICENSE
├── docs/
│   ├── architecture.md
│   ├── api_spec.md
│   └── deployment.md
├── server/
│   ├── app.py
│   ├── db.py
│   ├── models.py
│   ├── schemas.py
│   ├── util_sentiment.py
│   ├── requirements.txt
│   └── .env.example
├── client/
│   ├── index.html
│   ├── app.js
│   └── styles.css
├── corpus/
│   ├── README.md
│   ├── empathetic_dialogues.jsonl
│   └── routines.jsonl
├── tools/
│   ├── compliance_check.py
│   └── seed_data.py
└── tests/
    ├── test_api.py
    └── requirements.txt
```

## Unique & Innovative Aspects
- Focus on **empathetic elder care** (not a typical customer-service bot)
- **Memory Vault** for meaningful, personalized conversations
- **Privacy-first**: simple local SQLite for demo; can be swapped for on-device storage
- **Corpus** tailored for supportive, routine, reminder and reminiscence dialogues

## License
MIT — see `LICENSE`.
