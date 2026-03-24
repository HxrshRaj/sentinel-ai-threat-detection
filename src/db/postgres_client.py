class PostgresClient:
    def __init__(self):
        self.storage = []

    def insert_event(self, event: dict, result: dict):
        """
        Simulates inserting data into PostgreSQL
        """
        record = {
            "event": event,
            "result": result
        }
        self.storage.append(record)

        print("Saved to DB:", record)