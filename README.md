# sentinel-ai-threat-detection
# SentinelAI: AI-Powered Threat Simulation Framework

A simulated AI-based threat detection system that processes real-time event streams and detects anomalies using a modular data pipeline.

##  Features

- Real-time event streaming simulation
- Anomaly detection using threshold-based logic (ML-inspired)
- Modular pipeline architecture
- Simulated PostgreSQL data storage layer
- Scalable and extensible design

##  Architecture

The system consists of three main components:

1. **Data Pipeline**
   - Generates continuous event streams (CPU, Memory, Network)

2. **Anomaly Detector**
   - Identifies abnormal patterns based on predefined thresholds

3. **Postgres Client (Simulated)**
   - Stores processed events and detection results

##  How It Works

1. Generate event data continuously  
2. Pass event to anomaly detector  
3. Detect abnormal patterns  
4. Store results in database layer  

## 🛠 Tech Stack

- Python
- Modular Architecture
- Simulated Streaming Pipeline

## 📂 Project Structure
src/
├── data_pipeline.py
├── model/
│ └── anomaly_model.py
├── db/
│ └── postgres_client.py

## ▶️ How to Run

```bash
python src/data_pipeline.py

 Future Improvements:
Integrate real PostgreSQL database
Use PyTorch-based anomaly detection
Add real-time dashboards (Grafana/Prometheus)
Deploy using Docker and Kubernetes
👨‍💻 Author

Harsh Raj