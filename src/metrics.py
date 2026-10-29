def calculate_aov(df):
    return df["revenue"].mean()


def get_order_value_stats(df):
    return df["revenue"].describe()

def revenue_by_category(df):
    return (
        df.groupby("category")
        .agg(total_intäkt=("revenue", "sum"))
        .reset_index()
        .sort_values("total_intäkt", ascending=False)
        .reset_index(drop=True)
    )

def top_categories(df, n=3):
    return revenue_by_category(df).head(n)

