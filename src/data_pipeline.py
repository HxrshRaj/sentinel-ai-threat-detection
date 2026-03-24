import random
import time
from model.anomaly_model import AnomalyDetector
from db.postgres_client import PostgresClient

detector = AnomalyDetector()
db = PostgresClient()

def generate_event():
    return {
        "cpu_usage": random.uniform(0, 100),
        "memory_usage": random.uniform(0, 100),
        "network_traffic": random.uniform(0, 1000)
    }

def stream_data():
    while True:
        event = generate_event()
        result = detector.detect(event)

        # Save to DB
        db.insert_event(event, result)

        print("Event:", event)
        print("Anomaly Result:", result)
        print("-" * 50)

        time.sleep(1)

if __name__ == "__main__":
    stream_data()