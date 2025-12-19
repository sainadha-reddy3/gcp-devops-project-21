# GCP DevOps Project 21 🚀

End-to-end DevOps project implemented on **Google Cloud Platform (GCP)** demonstrating **CI/CD, containerization, Kubernetes orchestration, Ingress-based load balancing, and autoscaling (HPA)**.

This project is a **GCP equivalent of a real-world AWS DevOps project**, built to showcase production-grade DevOps practices.

---

## 🧩 Architecture Overview

Developer (GitHub)
|
v
Cloud Build (CI/CD)
|
v
Artifact Registry (Docker Images)
|
v
Google Kubernetes Engine (GKE)
|
v
Service + Ingress
|
v
GCP HTTP Load Balancer
|
v
Users / Traffic

yaml
Copy code

---

## 🔧 Tech Stack Used

- **Cloud Provider**: Google Cloud Platform (GCP)
- **CI/CD**: Google Cloud Build
- **Containerization**: Docker
- **Container Registry**: Artifact Registry
- **Orchestration**: Google Kubernetes Engine (GKE)
- **Load Balancing**: GCP HTTP Load Balancer (via Ingress)
- **Autoscaling**: Horizontal Pod Autoscaler (HPA)
- **Language**: Python (Flask)
- **Version Control**: GitHub

---

## 📁 Repository Structure

gcp-devops-project-21/
│
├── app/
│ ├── app.py # Flask application
│ └── requirements.txt # Python dependencies
│
├── k8s/
│ ├── deployment.yaml # Kubernetes Deployment
│ ├── service.yaml # Kubernetes Service
│ ├── ingress.yaml # Ingress (GCP Load Balancer)
│ └── hpa.yaml # Horizontal Pod Autoscaler
│
├── Dockerfile # Docker image definition
├── cloudbuild.yaml # Cloud Build CI/CD pipeline
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Application Details

- Simple **Flask web application**
- Endpoints:
  - `/` → Application response
  - `/health` → Health check for Kubernetes & Load Balancer
- Runs on **port 8080**

---

## 🔄 CI/CD Pipeline (Cloud Build)

Cloud Build pipeline performs:

1. **Build Docker Image**
2. **Push Image to Artifact Registry**
3. **Deploy Updated Image to GKE**

### cloudbuild.yaml (high-level)
- Uses `$BUILD_ID` for unique image tagging
- Updates Kubernetes Deployment using `kubectl set image`
- Fully automated deployment flow

---

## ☸️ Kubernetes Components Explained

### Deployment
- Runs the containerized application
- Includes **CPU & memory requests** (required for HPA)
- Ensures pod self-healing

### Service
- Internal stable networking (ClusterIP)
- Load balances traffic across pods

### Ingress
- Provisions **GCP HTTP Load Balancer**
- Exposes application publicly
- Assigns external IP automatically

### HPA (Horizontal Pod Autoscaler)
- Scales pods based on **CPU utilization**
- Min replicas: `1`
- Max replicas: `5`
- Target CPU: `50%`

---

## 📈 Autoscaling Demonstration (HPA)

- Traffic spike → CPU increases
- HPA scales pods automatically
- Traffic drops → pods scale down
- **No redeploy required**

This proves why **Kubernetes matters even after CI/CD succeeds**.

---

## 🌐 Public Access

Application is exposed using **GCP Ingress**:

http://<EXTERNAL-IP>

sql
Copy code

Health check:
http://<EXTERNAL-IP>/health

yaml
Copy code

---

## 🔍 How to Verify from GCP Console

- **Cloud Build** → CI/CD execution logs
- **Artifact Registry** → Docker image versions
- **Kubernetes Engine → Workloads** → Pod & Deployment health
- **Services & Ingress** → External IP
- **Load Balancing** → Backend services & health checks

---

## 🎯 Key DevOps Concepts Demonstrated

- CI/CD automation
- Immutable infrastructure
- Container lifecycle management
- Kubernetes self-healing
- Autoscaling under load
- Separation of build-time and run-time responsibilities
- Cloud-native load balancing

---

## 🧠 Interview-Ready Summary

> “This project demonstrates an end-to-end GCP DevOps workflow where Cloud Build handles CI/CD, Artifact Registry stores versioned images, GKE manages runtime orchestration, Ingress provisions a GCP Load Balancer, and HPA ensures autoscaling based on real traffic.”

---

## 📌 Future Improvements

- GitHub → Cloud Build triggers
- HTTPS with managed certificates
- Monitoring dashboards & alerts
- Terraform-based infrastructure provisioning

---

## 👤 Author

**Sainadh Reddy**  
DevOps Engineer (Intern)  
Focused on Kubernetes, GCP, CI/CD, and Cloud Infrastructure
