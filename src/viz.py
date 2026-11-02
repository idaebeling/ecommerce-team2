
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates


def plot_revenue_by_category(category_df):
   
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.bar(
        category_df["category"],
        category_df["total_intäkt"],
        color="skyblue"
    )

    ax.set_title("Total intäkt per produktkategori")
    ax.set_xlabel("Produktkategori")
    ax.set_ylabel("Total intäkt (SEK)")


    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(
            lambda x, pos: f"{x:,.0f}".replace(",", " ")
        )
    )


    for bar in ax.patches:
        ax.annotate(
            f"{bar.get_height():,.0f}".replace(",", " "),
            (
                bar.get_x() + bar.get_width() / 2,
                bar.get_height()
            ),
            ha="center",
            va="bottom",
            fontsize=8
        )


    ax.grid(axis="y", linestyle="--", alpha=0.3)
    ax.tick_params(axis="x", rotation=30)

    fig.tight_layout()

    plt.close(fig)

    return fig


def plot_monthly_revenue(monthly_df):
  
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        monthly_df["month"],
        monthly_df["total_intäkt"],
        marker="o"
    )

    ax.set_title("Månadsvis försäljningsintäkt")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Total intäkt (SEK)")

    ax.xaxis.set_major_formatter(
        mdates.DateFormatter("%Y-%m")
    )

    ax.xaxis.set_major_locator(
        mdates.MonthLocator(interval=1)
    )

    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(
            lambda x, pos: f"{x:,.0f}".replace(",", " ")
        )
    )

    ax.grid(True, linestyle="--", alpha=0.3)
    ax.tick_params(axis="x", rotation=45)

    fig.tight_layout()

    plt.close(fig)
    
    return fig
