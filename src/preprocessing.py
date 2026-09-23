def preprocess_data(input_df, preprocessing_params):

    output_df = input_df.copy()

    # Missing-value imputation
    output_df["monthly_income_imp"] = output_df["monthly_income"].fillna(
        preprocessing_params["imputation_values"]["monthly_income"]
    )

    # Special-value replacement
    output_df["age_imp"] = output_df["age"].replace(
        preprocessing_params["special_value_replacements"]["age"]
    )

    output_df["n_dpd_90plus_hist_imp"] = output_df["n_dpd_90plus_hist"].replace(
        preprocessing_params["special_value_replacements"]["n_dpd_90plus_hist"]
    )

    output_df["n_dpd_30_50_l2yrs_imp"] = output_df["n_dpd_30_50_l2yrs"].replace(
        preprocessing_params["special_value_replacements"]["n_dpd_30_50_l2yrs"]
    )

    return output_df