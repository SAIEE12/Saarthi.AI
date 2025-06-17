from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ? Replace with your real DB URL (e.g., PostgreSQL later)
SQLALCHEMY_DATABASE_URL = "sqlite:///./saarthi.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}  # For SQLite only
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ? THIS is what you're missing:
Base = declarative_base()

# Optional: Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
