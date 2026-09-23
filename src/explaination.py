import seaborn as sns
import matplotlib.pyplot as plt
from src.prediction import predict_pd
from src.preprocessing import preprocess_data
from src.woe_transformations import apply_woe_transformation

def calc_var_contri(input_df, processing_params, model):
    """
    Calculate the contribution of each feature to the model's prediction.
    """
    preprocessed_df = preprocess_data(
        input_df, 
        processing_params
    )

    woe_transformed_df = apply_woe_transformation(
        preprocessed_df
    )

    coefficients = model.params.drop("const")
    contributions = coefficients * woe_transformed_df[coefficients.index].iloc[0]

    var_contri_table = contributions.reset_index()
    var_contri_table.columns = ["var", "contri"]
    var_contri_table["abs_contri"] = var_contri_table["contri"].abs()

    return var_contri_table


def get_key_risk_drivers(var_contri_table, vars_desc_mapper, top_n=3):
    """
    Get the top N key risk drivers based on their contribution to the predicted default probability.
    """
    var_contri_data = var_contri_table.copy()

    var_contri_data = var_contri_data.sort_values(
        by="abs_contri",
        ascending=False
    )

    top_contributors = var_contri_data.head(top_n)
    top_contributors["variable_desc"] = top_contributors["var"].map(vars_desc_mapper)

    return top_contributors["variable_desc"]


def assess_customer(input_df, preprocessing_params, vars_desc_mapper, model):
    """
    Generate the complete credit-risk assessment for a customer.

    Returns:
        predicted_probability: Predicted probability of default.
        var_contri_table: Contribution of each model variable.
        key_risk_drivers: Top key risk drivers.
    """

    # Predict default probability
    predicted_pd = predict_pd(
        input_df,
        preprocessing_params,
        model
    )

    # Calculate variable contributions
    var_contri_table = calc_var_contri(
        input_df,
        preprocessing_params,
        model
    )

    # Identify key risk drivers
    key_risk_drivers = get_key_risk_drivers(
        var_contri_table,
        vars_desc_mapper,
        3
    )

    return (
        predicted_pd,
        var_contri_table,
        key_risk_drivers
    )

