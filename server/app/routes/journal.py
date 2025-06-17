from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.journal import JournalEntryCreate, JournalEntryOut
from app.services import journal as journal_service
from app.config import get_db

router = APIRouter(prefix="/journal", tags=["Journal"])

@router.post("/", response_model=JournalEntryOut)
def create_entry(entry: JournalEntryCreate, db: Session = Depends(get_db)):
    return journal_service.create_journal_entry(db, entry)
