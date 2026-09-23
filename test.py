import pickle
import pandas as pd
from pathlib import Path
import statsmodels.api as sm
import matplotlib.pyplot as plt
from src.prediction import predict_pd
import src.explaination as explaination
from src.config import logit_var_desc_mapper
from src.preprocessing import preprocess_data
from src.woe_transformations import apply_woe_transformation

ROOT_DIR = Path(__file__).resolve().parent
MODEL_DIR = ROOT_DIR / "models"

with open(MODEL_DIR / "preprocessing_params.pkl", "rb") as f:
    preprocessing_params = pickle.load(f)

with open(MODEL_DIR / "logit_model.pkl", "rb") as f:
    logit_model = pickle.load(f)

new_customer = pd.DataFrame({
    "avg_util_unsec": [0.78],
    "n_dpd_90plus_hist": [0],
    "n_dpd_30_50_l2yrs": [98],
    "age": [61],
    "monthly_income": [5001.0],
    "debt_income_ratio": [0.81]
})
print(new_customer)

predicted_probability = predict_pd(new_customer, preprocessing_params, logit_model)
print(f"Predicted Default Probability: {predicted_probability * 100:.2f}%")

var_contri_table = explaination.calc_var_contri(
    new_customer, 
    preprocessing_params, 
    logit_model
)
print("\n", var_contri_table)

key_risk_drivers = explaination.get_key_risk_drivers(
    var_contri_table,
    logit_var_desc_mapper
)
print("\n", key_risk_drivers)

var_contri_chart = explaination.create_var_contri_chart(
    var_contri_table,
    logit_var_desc_mapper
)
plt.show()

predicted_probability, var_contri_table, key_risk_drivers = explaination.assess_customer(
    new_customer,
    preprocessing_params,
    logit_var_desc_mapper,
    logit_model
)

print(predicted_probability)
print(var_contri_table)
print(key_risk_drivers)

