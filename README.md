# Give Me Some Credit — Credit Risk ML

End-to-end **credit risk ML project** using the Kaggle *Give Me Some Credit* dataset to predict probability of default.

## Current Implementation

- Data preprocessing and missing/special-value handling
- **Weight of Evidence (WOE)** transformation
- **Logistic Regression** PD model
- Model explainability using variable-level contributions
- **FastAPI** prediction API
- **Streamlit** interactive application
- **Docker** containerization
- **Docker Compose** for multi-container deployment

## Architecture

```text
Streamlit
    ↓
FastAPI
    ↓
Preprocessing → WOE → Logistic Regression
    ↓
Probability of Default + Risk Drivers
```

## Tech Stack

**Python · Pandas · NumPy · Statsmodels · FastAPI · Streamlit · Docker · Docker Compose**

## Run with Docker

Make sure Docker Desktop is running, then from the project root:

```bash
docker compose up --build
```

Open the application:

```text
http://localhost:8501
```

FastAPI documentation:

```text
http://localhost:8000/docs
```

To stop the application:

```bash
docker compose down
```

## Project Roadmap

- Random Forest challenger model
- XGBoost challenger model
- Model performance comparison
- Model monitoring
- Cloud deployment
