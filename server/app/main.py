from fastapi import FastAPI
from app.routes import journal
from app.config import Base, engine

# ? Create DB tables (if not already created)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(journal.router)

@app.get("/")
def read_root():
    return {"msg": "Welcome to Saarthi.AI Backend"}
