# 🛡️ Network Security ML & MLOps Pipeline

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

An end-to-end, production-grade Machine Learning and MLOps pipeline engineered to detect and classify network security threats in real time. This system integrates automated experiment tracking, containerization, and continuous delivery to maintain zero-downtime deployments on AWS.

---

## 📌 Project Overview

Network security environments require low-latency, highly accurate threat classification to mitigate malicious cyber attacks before disruption occurs. This project implements an automated, scalable pipeline that not only trains and evaluates a high-performance **Scikit-Learn** model but also wraps it into a low-latency **FastAPI** REST service. 

To bridge the gap between data science and production engineering, the entire workflow is versioned, containerized using **Docker**, tracked via **MLflow & DagsHub**, and automatically deployed to an **AWS EC2** instance using **GitHub Actions**.

---

## 🚀 Key Performance Metrics

In cybersecurity threat detection, minimizing false negatives is critical. The deployment model was optimized heavily for **Recall** while maintaining a near-perfect overall harmonic mean (**F1-Score**).

| Metric | Score | Impact |
| :--- | :--- | :--- |
| **Recall** | **99.41%** | Ensures nearly zero false negatives; malicious packets are rarely missed. |
| **F1-Score** | **99.15%** | Demonstrates an exceptional balance between Precision and Recall. |
| **Latency** | **< 45ms** | Optimized inference execution for real-time traffic filtering. |

---

## 🏗️ System Architecture & MLOps Pipeline

```text
[ Data Ingestion & Prep ] ──> [ Model Training (Scikit-Learn) ]
                                       │
                                       ├──> [ MLflow & DagsHub Tracking ]
                                       ▼
                              [ FastAPI REST Service ]
                                       │
                                       ▼
                       [ Docker Containerization ]
                                       │
                                       ▼
                   [ GitHub Actions CI/CD Pipeline ]
                                       │
                                       ▼
                      [ AWS EC2 Production Server ]
