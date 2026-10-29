
import pandas as pd


def calculate_aov(df):
    return df["revenue"].mean()


def get_order_value_stats(df):
    return df["revenue"].describe()


def revenue_by_group(df, group_column):
    return (
        df.groupby(group_column)["revenue"]
        .sum()
        .sort_values(ascending=False)
        .rename("total_revenue")
        .reset_index()
    )



def revenue_by_category(df):
    return (
        df.groupby("category")
        .agg(total_intäkt=("revenue", "sum"))
        .reset_index()
        .sort_values(by="total_intäkt", ascending=False)
        .reset_index(drop=True)
    )


def revenue_by_city(df):
    return (
        df.groupby("city")
        .agg(total_intäkt=("revenue", "sum"))
        .reset_index()
        .sort_values(by="total_intäkt", ascending=False)
        .reset_index(drop=True)
    )


def revenue_by_month(df):
    monthly_df = df.copy()

    monthly_df["month"] = (
        monthly_df["date"].dt.to_period("M").dt.to_timestamp()
    )

    return (
        monthly_df.groupby("month", as_index=False)
        .agg(total_intäkt=("revenue", "sum"))
        .sort_values("month")
        .reset_index(drop=True)
    )

                  

                 