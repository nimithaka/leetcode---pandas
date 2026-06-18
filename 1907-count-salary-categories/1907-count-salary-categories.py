import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts["category"] = np.where(
        accounts["income"] > 50000,
        "High Salary",
        np.where(accounts["income"] < 20000, "Low Salary", "Average Salary")
    )
    counts_df = (
        accounts["category"].value_counts()
        .reindex(["High Salary", "Low Salary", "Average Salary"], fill_value=0)
        .reset_index(name="accounts_count")
    )
    return counts_df[['category', 'accounts_count']]
    