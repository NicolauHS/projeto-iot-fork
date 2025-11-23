from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
from src.controllers.sensor_controller import (
    save_sensor_data,
    list_sensor_data,
    list_by_sensor,
    get_latest_data,
    delete_record,
    register_sensor,
)

router = APIRouter()

class SensorInput(BaseModel):
    sensorId: str
    type: str
    value: float
    timestamp: str

class SensorRegister(BaseModel):
    sensorId: str
    type: str
    location: str

@router.post("/sensor/data")
def receive_data(data: SensorInput):
    return save_sensor_data(data)

@router.get("/sensor/data")
def get_all():
    return list_sensor_data()

# 1. Dados por ID do sensor
@router.get("/sensor/data/{sensorId}")
def get_by_sensor(sensorId: str):
    return list_by_sensor(sensorId)

# 2. Últimos registros de cada sensor
@router.get("/sensor/data/latest")
def get_latest():
    return get_latest_data()

# 3. Remover um registro específico
@router.delete("/sensor/data/{record_id}")
def delete_sensor_record(record_id: int):
    return delete_record(record_id)

# 4. Cadastrar sensores manualmente
@router.post("/sensor/register")
def create_sensor(sensor: SensorRegister):
    return register_sensor(sensor)