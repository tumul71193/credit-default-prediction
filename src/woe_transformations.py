def woe_transformation_n_dpd_90plus_hist_imp(value):

    if value < 0.50:
        return 0.368445
    else:
        return -2.280864

def woe_transformation_n_dpd_30_50_l2yrs_imp(value):

    if value < 0.50:
        return 0.513985

    elif value < 1.50:
        return -0.903654

    else:
        return -1.865336

def woe_transformation_avg_util_unsec(value):

    if value < 0.06:
        return 1.395448

    elif value < 0.13:
        return 1.196037

    elif value < 0.22:
        return 0.801477

    elif value < 0.30:
        return 0.571255

    elif value < 0.39:
        return 0.264197

    elif value < 0.49:
        return 0.042306

    elif value < 0.70:
        return -0.380305

    elif value < 0.90:
        return -0.889439

    else:
        return -1.396248

def woe_transformation_age_imp(value):

    if value < 29.50:
        return -0.618478

    elif value < 36.50:
        return -0.502841

    elif value < 43.50:
        return -0.326797

    elif value < 47.50:
        return -0.210692

    elif value < 49.50:
        return -0.171605

    elif value < 52.50:
        return -0.130183

    elif value < 55.50:
        return -0.026589

    elif value < 59.50:
        return 0.253172

    elif value < 62.50:
        return 0.369651

    elif value < 67.50:
        return 0.726566

    elif value < 74.50:
        return 1.040110

    else:
        return 1.248390

def woe_transformation_monthly_income_imp(value):

    if value < 1508.50:
        return -0.099183

    elif value < 2569.50:
        return -0.394654

    elif value < 3331.50:
        return -0.469783

    elif value < 4833.50:
        return -0.229363

    elif value < 5333.50:
        return -0.062597

    elif value < 6643.50:
        return 0.117460

    elif value < 7656.50:
        return 0.197259

    elif value < 9945.50:
        return 0.281425

    else:
        return 0.460761

def woe_transformation_debt_income_ratio(value):

    if value < 0.02:
        return 0.297162

    elif value < 0.35:
        return 0.118882

    elif value < 0.42:
        return 0.057786

    elif value < 0.51:
        return -0.088438

    elif value < 0.65:
        return -0.321729

    elif value < 3.97:
        return -0.596973

    elif value < 995.50:
        return 0.063366

    else:
        return 0.328563


def apply_woe_transformation(input_df):

    output_df = input_df.copy()

    output_df["n_dpd_90plus_hist_imp_woe"] = output_df["n_dpd_90plus_hist_imp"].apply(woe_transformation_n_dpd_90plus_hist_imp)
    output_df["n_dpd_30_50_l2yrs_imp_woe"] = output_df["n_dpd_30_50_l2yrs_imp"].apply(woe_transformation_n_dpd_30_50_l2yrs_imp)
    output_df["avg_util_unsec_woe"] = output_df["avg_util_unsec"].apply(woe_transformation_avg_util_unsec)
    output_df["age_imp_woe"] = output_df["age_imp"].apply(woe_transformation_age_imp)
    output_df["monthly_income_imp_woe"] = output_df["monthly_income_imp"].apply(woe_transformation_monthly_income_imp)
    output_df["debt_income_ratio_woe"] = output_df["debt_income_ratio"].apply(woe_transformation_debt_income_ratio)

    return output_df