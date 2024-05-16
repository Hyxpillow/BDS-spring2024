from matplotlib import pyplot as plt
import pandas as pd

def merge_google_trend(df: pd.DataFrame):
    trend = pd.read_csv("./datasets/google_trend.csv")
    trend["begin_date"] = pd.to_datetime(trend["begin_date"])
    trend["end_date"] = trend["begin_date"] + pd.DateOffset(days=7)
    trend["movie_count"] = 0
    trend["movie_gain"] = 0
    
    df["google_trend"] = 0
    for i, date in enumerate(df["release_date"]):
        interest = trend[(trend["begin_date"] <= date) & (date <= trend["end_date"])]["interest"].iloc[0]
        df.loc[i, ["google_trend"]] = interest
        
        trend.loc[(trend["begin_date"] <= date) & (date <= trend["end_date"]), ["movie_count"]] += 1
        if df.loc[i, ["profitable"]].iloc[0] == 1:
            trend.loc[(trend["begin_date"] <= date) & (date <= trend["end_date"]), ["movie_gain"]] += 1
    df = df.drop(["release_date"], axis=1)
    trend['cumulative_gain'] = trend['movie_gain'].cumsum()
    trend['cumulative_count'] = trend['movie_count'].cumsum()
    trend['cumulative_profitability'] = trend['cumulative_gain'] / trend['cumulative_count']

    _, ax1 = plt.subplots(figsize=(20, 10))
    ax1.plot(trend['begin_date'], trend['interest'],
             linewidth=5.0, label="Google Trend")

    trend.loc[0, 'cumulative_gain'] = 0
    ax2 = ax1.twinx()
    ax2.plot(trend['begin_date'], 
             trend['cumulative_profitability'], 
             color="orange",
             linewidth=5.0, label="Profitablity")
    trend.to_csv("tmp.csv")
    ax2.set_ylim(0.2, 0.8)
    ax1.figure.legend(fontsize=30)
    # plt.axis('off')
    # plt.legend()
    ax1.set_xlabel("date", fontsize=24)
    ax1.set_ylabel("Google Trend", fontsize=24)
    ax2.set_ylabel("Profitability", fontsize=24)
    plt.title("Google vs. Profitability", fontsize=24)
    plt.savefig("./figures/trend.pdf", format="pdf")
    plt.savefig("./figures/trend.png")
    plt.clf()
    return df