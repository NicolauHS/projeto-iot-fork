import time
import random
import requests
from datetime import datetime, timezone
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://projeto-iot-fork-production.up.railway.app"

ENDPOINT = f"{BASE_URL}/api/sensor/data"

INTERVAL_SECONDS = 5

# Get Bearer token from environment variable
API_TOKEN = os.getenv("AUTH_TOKEN", "your-default-token")

SENSORS = [
    {"sensorId": "T010", "type": "temperature"},   # Temperatura (°C)
    {"sensorId": "H010", "type": "humidity"},      # Umidade (%)
    {"sensorId": "L010", "type": "luminosity"},    # Luminosidade (lux, por exemplo)
    {"sensorId": "M010", "type": "motion"},        # Movimento (0 ou 1, booleano)
]


def generate_value(sensor_type: str) -> float:
    """Gera um valor aleatório coerente com o tipo de sensor."""
    if sensor_type == "temperature":
        return round(random.uniform(18.0, 30.0), 2)
    elif sensor_type == "humidity":
        return round(random.uniform(30.0, 90.0), 1)
    elif sensor_type == "luminosity":
        return round(random.uniform(0, 1000), 1)
    elif sensor_type == "motion":
        return random.choice([0, 1])
    else:
        return 0.0


def current_timestamp_iso() -> str:
    """Retorna timestamp no formato ISO 8601, em UTC."""
    return datetime.now(timezone.utc).isoformat()


def send_sensor_reading(sensor_id: str, sensor_type: str):
    """Monta o JSON e envia para a API."""
    payload = {
        "sensorId": sensor_id,
        "type": sensor_type,
        "value": generate_value(sensor_type),
        "timestamp": current_timestamp_iso(),
    }

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(ENDPOINT, json=payload, headers=headers, timeout=5)
        response.raise_for_status()
        print(f"[OK] Enviado: {payload}  Resposta: {response.status_code}")
    except requests.RequestException as e:
        print(f"[ERRO] Falha ao enviar leitura de {sensor_id} ({sensor_type}): {e}")


def main():
    print(f"Iniciando simulador de sensores IoT...")
    print(f"Enviando dados para: {ENDPOINT}")
    print(f"Token configurado: {'Sim' if API_TOKEN != 'your-default-token' else 'Não (usando default)'}")
    print("Pressione Ctrl+C para parar.\n")

    try:
        while True:
            for sensor in SENSORS:
                send_sensor_reading(sensor["sensorId"], sensor["type"])
                time.sleep(0.5)
            time.sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nSimulador encerrado pelo usuário.")


if __name__ == "__main__":
    main()
