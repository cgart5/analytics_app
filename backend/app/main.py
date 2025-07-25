from fastapi import FastAPI, HTTPException, Depends 
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from sqlalchemy.orm import Session
from database import SessionLocal, engine


app = FastAPI(
    title="Sports Analytics API",
    description="api to transfer live game stats and return ML insights",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

origins = [
    'http://localhost:3000'
]

# Cors are ways to defend against cross origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], #any method POST, GET, DELETE, UPDATE
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)

