import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_var_contri_chart(var_contri_data, vars_desc_mapper):
    """
    Create the variable contribution bar chart.
    """

    plot_data = pd.DataFrame(var_contri_data)

    plot_data = plot_data.sort_values(
        by="abs_contri",
        ascending=True
    )

    plot_data["variable_desc"] = plot_data["var"].map(
        vars_desc_mapper
    )

    plot_data["impact"] = plot_data["contri"].apply(
        lambda x: "Positive" if x > 0 else "Negative"
    )

    fig, ax = plt.subplots(figsize=(13, 8))

    sns.barplot(
        data=plot_data,
        x="contri",
        y="variable_desc",
        hue="impact",
        palette={
            "Positive": "red",
            "Negative": "blue"
        },
        dodge=False,
        legend=False,
        ax=ax
    )

    ax.invert_yaxis()

    ax.set_title("")

    ax.set_xlabel(
        "Contribution to Model Score",
        fontsize=16
    )

    ax.set_ylabel(
        "Variable",
        fontsize=16
    )

    ax.tick_params(
        axis="x",
        labelsize=15
    )

    ax.tick_params(
        axis="y",
        labelsize=15
    )

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1)

    ax.grid(False)

    plt.tight_layout()

    return fig