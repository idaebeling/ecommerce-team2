def calculate_aov(df):
    return df["revenue"].mean()


def get_order_value_stats(df):
    return df["revenue"].describe()