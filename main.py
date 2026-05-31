from fastapi import FastAPI
from database import engine, Base
from models.item import Item
from routers.item import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)