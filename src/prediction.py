import statsmodels.api as sm
from src.preprocessing import preprocess_data
from src.woe_transformations import apply_woe_transformation

def predict_pd(input_df, preprocessing_params, logit_model):
    """
    Preprocess the input data, apply WOE transformation, and predict default probability using the logistic regression model.
    """
    preprocessed_df = preprocess_data(input_df, preprocessing_params)
    woe_transformed_df = apply_woe_transformation(preprocessed_df)

    woe_transformed_df = sm.add_constant(
        woe_transformed_df, 
        has_constant="add"
    )

    model_variables = logit_model.params.index.tolist()
    X = woe_transformed_df[model_variables]
    predicted_probability = logit_model.predict(X).iloc[0]

    return predicted_probability