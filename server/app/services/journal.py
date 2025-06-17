from app.models.journal import JournalEntry
from app.schemas.journal import JournalEntryCreate
from sqlalchemy.orm import Session
import random

# Simulate AI until GPT-4 is integrated
def fake_ai_process(text: str):
    emotions = ['happy', 'sad', 'anxious', 'grateful', 'confused']
    return {
        "summary": "This is a short summary of your journal entry.",
        "emotion": random.choice(emotions)
    }

def create_journal_entry(db: Session, entry: JournalEntryCreate):
    ai_result = fake_ai_process(entry.content)

    db_entry = JournalEntry(
        content=entry.content,
        summary=ai_result["summary"],
        emotion=ai_result["emotion"]
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry
