import pandas as pd
def generate_label(df: pd.DataFrame):
    df["profitable"] = df["revenue"] / df["budget"]
    df["profitable"] = df["profitable"] > 1
    df["profitable"] = df["profitable"].astype(int)
    df = df.drop(["revenue"], axis=1)
    return df