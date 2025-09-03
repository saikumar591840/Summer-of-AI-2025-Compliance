# API Spec (v1)

Base URL: `http://localhost:8000/api`

## Health
- `GET /api/ping` → `{ "status": "ok", "time": "<iso>" }`

## Users
- `POST /api/users` → create caregiver or patient
  - body: `{ "name": "A", "role": "caregiver|patient" }`
- `GET /api/users` → list
- `GET /api/users/{id}` → retrieve

## Memories
- `POST /api/memories` → `{ "patient_id": 1, "title": "...", "content": "..." }`
- `GET /api/memories?patient_id=1`
- `DELETE /api/memories/{id}`

## Reminders
- `POST /api/reminders` → `{ "patient_id": 1, "text": "...", "time": "2025-09-03T09:00:00" }`
- `GET /api/reminders?patient_id=1`
- `DELETE /api/reminders/{id}`

## Chat
- `POST /api/chat`
  - body: `{ "patient_id": 1, "message": "I'm feeling lonely today" }`
  - response: `{ "reply": "..." , "sentiment": "positive|neutral|negative" }`
