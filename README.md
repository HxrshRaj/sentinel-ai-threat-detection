# SentinelAI: AI-Powered Threat Simulation Framework

A modular, AI-inspired threat detection system that simulates real-time event streams and identifies anomalies using a scalable data pipeline architecture.

## Features

- Real-time event streaming simulation (CPU, Memory, Network)
- Modular anomaly detection system
- Scalable pipeline design for data processing
- Simulated PostgreSQL data storage layer
- Designed for ML integration and cloud deployment

##  Architecture

The system consists of three main components:

1. **Data Pipeline**
   - Continuously generates and processes event streams

2. **Anomaly Detection Engine**
   - Detects abnormal system behavior using rule-based logic
   - Designed to support ML-based anomaly detection models

3. **Database Layer**
   - Simulates PostgreSQL storage for processed events and results

##  How It Works

1. Generate real-time system events  
2. Process events through anomaly detection logic  
3. Identify abnormal patterns  
4. Store results in database layer  

##  Machine Learning Integration

- Current implementation uses threshold-based detection as a baseline
- Architecture is designed to integrate ML models such as:
  - Autoencoders
  - PCA-based anomaly detection
  - PyTorch-based models (future integration)

##  Tech Stack

- Python
- Modular Pipeline Architecture
- Data Processing
- PostgreSQL (simulated)
- ML-ready design

## 📂 Project Structure
src/
├── data_pipeline.py
├── model/
│ └── anomaly_model.py
├── db/
│ └── postgres_client.py

##  How to Run

```bash
python src/data_pipeline.py

## Future Improvements
Integrate real PostgreSQL database
Implement ML models using PyTorch
Add monitoring tools (Grafana/Prometheus)
Deploy using Docker and Kubernetes

👨‍💻 Author
Harsh Raj

