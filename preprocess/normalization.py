import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def normalize(df: pd.DataFrame):
    for col in df.columns:
        if col == "profitable":
            continue
        std = df[col].std()
        mean = df[col].mean()
        df[col] = (df[col] - mean)/ std
    df = df.round(4)
    return df

def cal_cov_matrix(df: pd.DataFrame):
    df = df.copy().drop(['profitable'], axis=1)
    plt.figure(figsize=(12, 10))
    m = sns.heatmap(df.cov(), annot=True, cmap='coolwarm', fmt='.2f', annot_kws={"size": 16})
    m.set_yticklabels(m.get_yticklabels(), rotation=0)
    plt.savefig('./figures/covariance.pdf', format="pdf")
    plt.clf()
    return 