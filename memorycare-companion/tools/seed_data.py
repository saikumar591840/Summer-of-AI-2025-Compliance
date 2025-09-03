"""Seed demo data into the local database."""
from datetime import datetime, timedelta
from server.db import SessionLocal, Base, engine
from server import models

Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Create users
patient = models.User(name="Alex", role="patient")
caregiver = models.User(name="Jordan", role="caregiver")
db.add_all([patient, caregiver]); db.commit(); db.refresh(patient); db.refresh(caregiver)

# Memories
m1 = models.Memory(patient_id=patient.id, title="Beach picnic", content="Sunny day with family at the beach.")
m2 = models.Memory(patient_id=patient.id, title="Favorite Song", content="Listening to 'Que Sera, Sera' on the radio.")
db.add_all([m1, m2])

# Reminders
now = datetime.utcnow()
r1 = models.Reminder(patient_id=patient.id, text="Take evening medication", time=now + timedelta(hours=1))
r2 = models.Reminder(patient_id=patient.id, text="Call granddaughter", time=now + timedelta(hours=2))
db.add_all([r1, r2])

db.commit()
print("Seeded patient id:", patient.id)
