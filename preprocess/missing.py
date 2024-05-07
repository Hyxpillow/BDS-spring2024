import pandas as pd

def remove_missing_value(df: pd.DataFrame):
    df = df[df["core_actor"].notna()]
    df = df[df["actor_avg_age"] > 10]
    df.to_csv("datasets/clean.csv", index=False)
    df = pd.read_csv("datasets/clean.csv")

    return df