class AnomalyDetector:
    def __init__(self):
        # simple threshold values
        self.cpu_threshold = 85
        self.memory_threshold = 90
        self.network_threshold = 900

    def detect(self, event: dict):
        """
        Detect anomalies based on thresholds
        """
        anomalies = []

        if event["cpu_usage"] > self.cpu_threshold:
            anomalies.append("High CPU Usage")

        if event["memory_usage"] > self.memory_threshold:
            anomalies.append("High Memory Usage")

        if event["network_traffic"] > self.network_threshold:
            anomalies.append("High Network Traffic")

        if anomalies:
            return {
                "anomaly": True,
                "issues": anomalies
            }
        else:
            return {
                "anomaly": False,
                "issues": []
            }