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

    _, ax1 = plt.subplots(figsize=(20, 10))
    ax1.plot(trend['begin_date'], trend['interest'])

    ax2 = ax1.twinx()
    # y = []
    # for i, _count in enumerate(trend["movie_gain"]):
    #     if _count == 0:
    #         y.append(None)
    #     else:
    #         y.append(trend['movie_gain'][i])
    ax2.plot(trend['begin_date'], trend['movie_gain'], color="orange")
    # ax2.set_ylim(0, 6)

    plt.savefig("./figures/trend.pdf", format="pdf")
    plt.clf()
    return df