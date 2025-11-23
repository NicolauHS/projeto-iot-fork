from fastapi import FastAPI
from db.database import engine, Base
from src.routes.routes_model import router as sensor_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(sensor_router, prefix="/api")