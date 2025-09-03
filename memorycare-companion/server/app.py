from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional
import os

from .db import Base, engine, get_db
from . import models, schemas
from .util_sentiment import polarity

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI MemoryCare Companion API", version="1.0.0")

origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/ping")
def ping():
    return {"status": "ok", "time": datetime.utcnow().isoformat()}

# Users
@app.post("/api/users", response_model=schemas.UserOut)
def create_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    user = models.User(name=payload.name, role=payload.role)
    db.add(user); db.commit(); db.refresh(user)
    return user

@app.get("/api/users", response_model=List[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@app.get("/api/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    u = db.query(models.User).get(user_id)
    if not u:
        raise HTTPException(404, "User not found")
    return u

# Memories
@app.post("/api/memories", response_model=schemas.MemoryOut)
def create_memory(payload: schemas.MemoryCreate, db: Session = Depends(get_db)):
    patient = db.query(models.User).get(payload.patient_id)
    if not patient or patient.role != "patient":
        raise HTTPException(422, "Invalid patient_id")
    m = models.Memory(patient_id=payload.patient_id, title=payload.title, content=payload.content)
    db.add(m); db.commit(); db.refresh(m)
    return m

@app.get("/api/memories", response_model=List[schemas.MemoryOut])
def list_memories(patient_id: Optional[int] = None, db: Session = Depends(get_db)):
    q = db.query(models.Memory)
    if patient_id:
        q = q.filter(models.Memory.patient_id == patient_id)
    return q.order_by(models.Memory.created_at.desc()).all()

@app.delete("/api/memories/{memory_id}")
def delete_memory(memory_id: int, db: Session = Depends(get_db)):
    m = db.query(models.Memory).get(memory_id)
    if not m:
        raise HTTPException(404, "Not found")
    db.delete(m); db.commit()
    return {"deleted": True}

# Reminders
@app.post("/api/reminders", response_model=schemas.ReminderOut)
def create_reminder(payload: schemas.ReminderCreate, db: Session = Depends(get_db)):
    patient = db.query(models.User).get(payload.patient_id)
    if not patient or patient.role != "patient":
        raise HTTPException(422, "Invalid patient_id")
    r = models.Reminder(patient_id=payload.patient_id, text=payload.text, time=payload.time)
    db.add(r); db.commit(); db.refresh(r)
    return r

@app.get("/api/reminders", response_model=List[schemas.ReminderOut])
def list_reminders(patient_id: Optional[int] = None, db: Session = Depends(get_db)):
    q = db.query(models.Reminder)
    if patient_id:
        q = q.filter(models.Reminder.patient_id == patient_id)
    return q.order_by(models.Reminder.time.asc()).all()

@app.delete("/api/reminders/{reminder_id}")
def delete_reminder(reminder_id: int, db: Session = Depends(get_db)):
    r = db.query(models.Reminder).get(reminder_id)
    if not r:
        raise HTTPException(404, "Not found")
    db.delete(r); db.commit()
    return {"deleted": True}

# Chat (demo: empathetic + memory-aware)
@app.post("/api/chat", response_model=schemas.ChatOut)
def chat(payload: schemas.ChatIn, db: Session = Depends(get_db)):
    patient = db.query(models.User).get(payload.patient_id)
    if not patient or patient.role != "patient":
        raise HTTPException(422, "Invalid patient_id")
    sentiment = polarity(payload.message)
    # Fetch 1-2 recent memories to personalize
    mem = db.query(models.Memory).filter(models.Memory.patient_id == patient.id).order_by(models.Memory.created_at.desc()).limit(2).all()
    mem_hint = "; ".join([f"{m.title}" for m in mem]) if mem else ""
    templates = {
        "positive": "That sounds lovely. {mem} Would you like to tell me more about it?",
        "neutral" : "I'm here with you. {mem} What would you like to chat about now?",
        "negative": "I'm sorry you're feeling this way. {mem} Would a short breathing exercise or a favorite song help?"
    }
    base = templates.get(sentiment, templates["neutral"])
    mem_text = f"Remember: {mem_hint}" if mem_hint else "Let's think of a nice memory together."
    reply = base.format(mem=mem_text)
    return {"reply": reply, "sentiment": sentiment}
