import pandas as pd

def normalize(df: pd.DataFrame):
    for col in df.columns:
        if col == "profitable":
            continue
        std = df[col].std()
        mean = df[col].mean()
        df[col] = (df[col] - mean)/ std
    df = df.round(4)
    return df