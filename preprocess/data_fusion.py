import pandas as pd

def merge_google_trend(df: pd.DataFrame):
    trend = pd.read_csv("./preprocess/trend.csv")
    trend["begin_date"] = pd.to_datetime(trend["begin_date"])
    trend["end_date"] = trend["begin_date"] + pd.DateOffset(days=7)
    df["google_trend"] = 0
    for i, date in enumerate(df["release_date"]):
        interest = trend[(trend["begin_date"] <= date) & (date <= trend["end_date"])]["interest"].iloc[0]
        df.loc[i, ["google_trend"]] = interest
    df = df.drop(["release_date"], axis=1)
    return df