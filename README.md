# 🏠 House Price Prediction API (Machine Learning + FastAPI)

This project is an end-to-end **Machine Learning Engineer** project that trains a regression model and serves predictions through a **FastAPI** backend.

---

## 🚀 Project Overview

- Train a machine learning model to predict house prices  
- Compare Linear Regression vs Random Forest  
- Save the best-performing model  
- Deploy the model using FastAPI  
- Expose a `/predict` REST API endpoint  

---

## 🧠 Tech Stack

- Python 3.10+
- scikit-learn
- pandas
- numpy
- FastAPI
- Uvicorn
- joblib

---

## 📁 Project Structure

```

ml-house-price/
│
├── app/
│ ├── main.py # FastAPI app
│ └── schemas.py # Pydantic request models
│
├── models/
│ └── house_model.pkl # Trained ML model
│
├── notebooks/
│ └── train.ipynb # Data analysis & model training
│
├── requirements.txt
└── README.

```


## 🧠 Quick reinforcement (important)

👉 **Why `requirements.txt` matters?**  
Because anyone (recruiter, teammate, server) can run:

```bash
pip install -r requirements.txt
