from sqlalchemy import func
from db.database import SessionLocal
from src.models.sensor_model import SensorData
from collections import defaultdict

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

def list_by_sensor(sensorId):
    db = SessionLocal()
    return db.query(SensorData).filter(SensorData.sensorId == sensorId).all()

def get_grouped_data():
    all_data = list_sensor_data()
    
    grouped = defaultdict(list)
    for record in all_data:
        grouped[record.sensorId].append({
            "value": record.value,
            "timestamp": record.timestamp
        })
    
    return dict(grouped)

def get_latest_data():
    db = SessionLocal()
    subquery = db.query(
        SensorData.sensorId,
        func.max(SensorData.timestamp).label("max_timestamp")
    ).group_by(SensorData.sensorId).subquery()

    latest_data = db.query(SensorData).join(
        subquery,
        (SensorData.sensorId == subquery.c.sensorId) &
        (SensorData.timestamp == subquery.c.max_timestamp)
    ).all()

    return latest_data

def delete_record(record_id):
    db = SessionLocal()
    record = db.query(SensorData).filter(SensorData.id == record_id).first()
    if record:
        db.delete(record)
        db.commit()
        return {"status": "deleted"}
    return {"status": "not found"}

def register_sensor(sensorId):
    db = SessionLocal()
    existing = db.query(SensorData).filter(SensorData.sensorId == sensorId).first()
    if existing:
        return {"status": "already registered"}
    new_sensor = SensorData(sensorId=sensorId, value=0.0, timestamp="")
    db.add(new_sensor)
    db.commit()
    return {"status": "registered"}