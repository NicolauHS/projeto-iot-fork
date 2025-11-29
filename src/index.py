from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine, Base
from src.routes.routes_model import router as sensor_router

app = FastAPI()

origins = [
    "http://localhost:8000", # testing
    "http://localhost:8080", # testing
    "https://devnicolas.com.br/sensor-dash", #production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(sensor_router, prefix="/api")
