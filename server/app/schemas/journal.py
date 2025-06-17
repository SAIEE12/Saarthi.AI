from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JournalEntryCreate(BaseModel):
    content: str

class JournalEntryOut(BaseModel):
    id: int
    content: str
    summary: str
    emotion: str
    created_at: datetime

    model_config = {"from_attributes": True}
