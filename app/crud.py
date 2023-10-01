from sqlalchemy.orm import Session
from . import models, schemas


def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()


def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()


def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def update_client(db: Session, client: schemas.Client):
    db.query(models.Client).filter(models.Client.id == client.id).update(client.dict())
    db.commit()
    return get_client(db, client.id)


def delete_client(db: Session, client_id: int):
    db.query(models.Client).filter(models.Client.id == client_id).delete()
    db.commit()
