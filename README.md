# 🚗 Vehicle Insurance End-to-End ML Project

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20S3-orange?logo=amazon-aws)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blueviolet?logo=github-actions)

---

## 📖 Overview

A robust, production-ready machine learning pipeline for predicting vehicle insurance outcomes. This project covers the full ML lifecycle: data ingestion, validation, transformation, model training, evaluation, deployment, and serving predictions via a modern web interface. The solution is cloud-native, leveraging AWS S3 for model storage, EC2 for deployment, and CI/CD for automation.

---

## 🚀 Features

- **Automated Data Ingestion, Validation, and Transformation**
- **Model Training, Evaluation, and Selection**
- **Seamless Model Storage and Retrieval from AWS S3**
- **User-Friendly Web App for Real-Time Predictions**
- **CI/CD Pipeline for Continuous Integration and Deployment**
- **Production Deployment on AWS EC2**
- **Comprehensive Logging and Error Handling**

---

## 🗂️ Project Structure

```
Proj-Vehicle_insurance-end_to_end/
│
├── app.py                  # Main web application
├── demo.py                 # Demo script
├── Dockerfile              # Docker containerization
├── requirements.txt        # Python dependencies
├── setup.py                # Package setup
├── config/                 # YAML configs for model & schema
├── notebook/               # Jupyter notebooks & datasets
├── src/                    # Source code (components, pipelines, utils, etc.)
├── static/                 # Static files (CSS)
├── templates/              # HTML templates
├── logs/                   # Log files
└── README.md               # Project documentation
```

---

## ⚙️ End-to-End Workflow

1. **Data Ingestion:** Raw vehicle data is ingested and validated.
2. **Data Transformation:** Data is cleaned, encoded, and prepared for modeling.
3. **Model Training & Evaluation:** ML models are trained, evaluated, and the best model is selected.
4. **Model Pushing:** The production model is uploaded to AWS S3.
5. **Web App Deployment:** The app is deployed on AWS EC2, serving predictions via a user-friendly interface.
6. **CI/CD Automation:** GitHub Actions (or your chosen CI/CD tool) automates testing, building, and deployment to EC2.

---

## ☁️ Cloud & DevOps

- **AWS S3:** Stores the trained model (`model.pkl`) for production use.
- **AWS EC2:** Hosts the web application for public access.
- **CI/CD:** Automates deployment after every push to the main branch.

---

## 🖥️ Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Proj-Vehicle_insurance-end_to_end.git
   cd Proj-Vehicle_insurance-end_to_end
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```bash
   python app.py
   ```
   The app will be available at [http://localhost:5000](http://localhost:5000).

---

## 🌐 Deployment on AWS EC2

1. **Launch an EC2 instance** (Ubuntu recommended, t2.micro for testing; larger for production).
2. **Open required ports** (e.g., 5000, 80) in the Security Group.
3. **SSH into your instance** and clone the repo.
4. **Install Python and dependencies.**
5. **Set up AWS credentials** for S3 access.
6. **Run the app:**
   ```bash
   python app.py --host 0.0.0.0 --port 5000
   ```
7. **Access the app** via your EC2 public IP:  
   `http://<your-ec2-public-ip>:5000`

---

## 🔄 CI/CD Pipeline

- **Automated Build & Test:** Every push triggers the pipeline to build, test, and deploy the latest code to EC2.
- **Zero-downtime Deployment:** The app is restarted automatically after deployment.
- **Easy Rollback:** Previous versions can be redeployed if needed.

---

## 📝 Usage

- Visit the web app.
- Enter vehicle data in the form.
- Click "Predict" to get insurance predictions instantly.

---

## 🛠️ Tech Stack

- **Python 3.10**
- **FastAPI**
- **scikit-learn**
- **AWS S3, EC2**
- **GitHub Actions** (or your CI/CD tool)
- **Docker** (optional)

---
