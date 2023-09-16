from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas
from .database import SessionLocal, engine, Base

app = FastAPI()


def create_tables():
    Base.metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup_event():
    create_tables()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db=db, client=client)


@app.get("/clients/", response_model=List[schemas.Client])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = crud.get_clients(db=db, skip=skip, limit=limit)
    return clients


@app.get("/clients/{client_id}", response_model=schemas.Client)
def read_client(client_id: int, db: Session = Depends(get_db)):
    client = crud.get_client(db=db, client_id=client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client


@app.put("/clients/{client_id}", response_model=schemas.Client)
def update_client(
    client_id: int, client: schemas.ClientCreate, db: Session = Depends(get_db)
):
    return crud.update_client(db=db, client=client)


@app.delete("/clients/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    crud.delete_client(db=db, client_id=client_id)
