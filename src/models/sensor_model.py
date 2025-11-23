from sqlalchemy import Column, Integer, String, Float
from db.database import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    sensorId = Column(String)
    value = Column(Float)
    timestamp = Column(String)