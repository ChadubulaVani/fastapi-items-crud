from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.item import Item
from schemas.item import ItemCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


## CREATE

@router.post("/items")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):

    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


## READ ALL

@router.get("/items")
def get_items(db: Session = Depends(get_db)):
    return db.query(Item).all()


## READ ONE

@router.get("/items/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    return db.query(Item).filter(Item.id == item_id).first()

## UPDATE

@router.put("/items/{item_id}")
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):

    db_item = db.query(Item).filter(Item.id == item_id).first()

    db_item.name = item.name
    db_item.description = item.description

    db.commit()
    db.refresh(db_item)

    return db_item


## DELETE

@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):

    db_item = db.query(Item).filter(Item.id == item_id).first()

    db.delete(db_item)
    db.commit()

    return {"message": "Item deleted"}