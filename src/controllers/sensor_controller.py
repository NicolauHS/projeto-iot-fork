from db.database import SessionLocal
from src.models.sensor_model import SensorData

def save_sensor_data(data):
    db = SessionLocal()
    registro = SensorData(
        sensorId=data.sensorId,
        value=data.value,
        timestamp=data.timestamp,
    )
    db.add(registro)
    db.commit()
    return {"status": "ok"}

def list_sensor_data():
    db = SessionLocal()
    return db.query(SensorData).all()