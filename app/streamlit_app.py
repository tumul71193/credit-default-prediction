import os
import requests
import streamlit as st
import matplotlib.pyplot as plt
from src.config import logit_var_desc_mapper
from app.streamlit_utils import create_var_contri_chart

st.title("Credit Risk Prediction")

st.write(
    "Enter customer information to estimate the probability of serious delinquency."
)

age = st.number_input(
    "Age",
    min_value=0.0,
    step=1.0
)

monthly_income = st.number_input(
    "Monthly Income",
    min_value=0.0,
    step=100.0
)

n_dpd_90plus_hist = st.number_input(
    "Number of 90+ DPDs in History",
    min_value=0,
    step=1
)

n_dpd_30_50_l2yrs = st.number_input(
    "Number of 30–50 DPDs in Last 2 Years",
    min_value=0,
    step=1
)

avg_util_unsec = st.number_input(
    "Average Utilization of Unsecured Lines",
    min_value=0.0,
    step=0.01
)

debt_income_ratio = st.number_input(
    "Debt-to-Income Ratio",
    min_value=0.0,
    step=0.01
)

API_URL = os.getenv("FASTAPI_URL", "http://127.0.0.1:8000")

if st.button("Predict"):

    customer_data = {
        "age": age,
        "monthly_income": monthly_income,
        "n_dpd_90plus_hist": n_dpd_90plus_hist,
        "n_dpd_30_50_l2yrs": n_dpd_30_50_l2yrs,
        "avg_util_unsec": avg_util_unsec,
        "debt_income_ratio": debt_income_ratio
    }

    response = requests.post(
        f"{API_URL}/predict",
        json=customer_data
    )

    if response.status_code == 200:
        result = response.json()
        st.success("Prediction completed.")
        # st.write(result)

        predicted_probability = result["predicted_default_probability"]
        st.metric(
            "Predicted Default Probability",
            f"{predicted_probability * 100:.2f}%"
        )

        st.subheader("Key Risk Drivers")
        for driver in result["key_risk_drivers"].values():
            st.write(f"- {driver}")

        st.subheader("Variable Contributions")
        fig = create_var_contri_chart(
            result["variable_contributions"], 
            logit_var_desc_mapper
        )
        st.pyplot(fig)

    else:
        st.error(
            f"API request failed with status code {response.status_code}"
        )

