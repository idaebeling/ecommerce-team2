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
