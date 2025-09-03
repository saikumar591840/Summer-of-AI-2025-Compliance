from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List

class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    role: str = Field(..., pattern="^(caregiver|patient)$")

class UserOut(BaseModel):
    id: int
    name: str
    role: str
    created_at: datetime

    class Config:
        from_attributes = True

class MemoryCreate(BaseModel):
    patient_id: int
    title: str
    content: str

class MemoryOut(BaseModel):
    id: int
    patient_id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True

class ReminderCreate(BaseModel):
    patient_id: int
    text: str
    time: datetime

class ReminderOut(BaseModel):
    id: int
    patient_id: int
    text: str
    time: datetime
    created_at: datetime

    class Config:
        from_attributes = True

class ChatIn(BaseModel):
    patient_id: int
    message: str

class ChatOut(BaseModel):
    reply: str
    sentiment: str
