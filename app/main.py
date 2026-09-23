import pickle
import pandas as pd
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel, Field
from src.explaination import assess_customer
from src.config import logit_var_desc_mapper

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_DIR = PROJECT_ROOT / "models"

with open(MODEL_DIR / "preprocessing_params.pkl", "rb") as f:
    preprocessing_params = pickle.load(f)

with open(MODEL_DIR / "logit_model.pkl", "rb") as f:
    logit_model = pickle.load(f)

class CustomerInput(BaseModel):
    age: float = Field(ge=0)
    monthly_income: float | None = Field(default=None, ge=0)
    n_dpd_90plus_hist: int = Field(ge=0)
    n_dpd_30_50_l2yrs: int = Field(ge=0)
    avg_util_unsec: float = Field(ge=0)
    debt_income_ratio: float = Field(ge=0)

app = FastAPI(
    title = "Credit Risk PD API",
    description = "API for predicting probability of default and explaining model predictions.",
    version = "1.0.0"
)

@app.get("/")
def home():
    return {"message": "Credit Risk PD API is running"}

@app.post("/predict")
def predict(customer: CustomerInput):

    customer_df = pd.DataFrame(
        [customer.model_dump()]
    )

    predicted_probability, var_contri_table, key_risk_drivers = assess_customer(
        customer_df,
        preprocessing_params,
        logit_var_desc_mapper,
        logit_model
    )

    return {
        "predicted_default_probability": float(predicted_probability),
        "variable_contributions": var_contri_table.to_dict(orient="records"),
        "key_risk_drivers": key_risk_drivers
    }

