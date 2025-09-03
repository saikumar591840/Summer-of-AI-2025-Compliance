from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    role = Column(String(20), nullable=False)  # caregiver | patient
    created_at = Column(DateTime, default=datetime.utcnow)

    memories = relationship("Memory", back_populates="patient")
    reminders = relationship("Reminder", back_populates="patient")

class Memory(Base):
    __tablename__ = "memories"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    patient = relationship("User", back_populates="memories")

class Reminder(Base):
    __tablename__ = "reminders"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    text = Column(String(300), nullable=False)
    time = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    patient = relationship("User", back_populates="reminders")
