import math
from matplotlib import pyplot as plt
import pandas as pd

def binning(df: pd.DataFrame):
    df = df.copy()
    df = binning_runtime(df)
    df = binning_budget(df)
    df = binning_vote_average(df)
    df = binning_popularity(df)
    df = binning_google_trend(df)
    return df

def binning_runtime(df: pd.DataFrame):
    a = df["runtime"].quantile(0.25)
    b = df["runtime"].quantile(0.5)
    c = df["runtime"].quantile(0.75)
    df["A"] = 0
    df.loc[df["runtime"] >= a, "A"] = 1
    df.loc[df["runtime"] >= b, "A"] = 2
    df.loc[df["runtime"] >= c, "A"] = 3
    df = df.drop(["runtime"], axis=1)
    df = df.rename(columns={'A': 'runtime'}, inplace=False)
    return df

def binning_budget(df: pd.DataFrame):
    a = df["budget"].quantile(0.25)
    b = df["budget"].quantile(0.5)
    c = df["budget"].quantile(0.75)
    df["A"] = 0
    df.loc[df["budget"] >= a, "A"] = 1
    df.loc[df["budget"] >= b, "A"] = 2
    df.loc[df["budget"] >= c, "A"] = 3
    df = df.drop(["budget"], axis=1)
    df.rename(columns={'A': 'budget'}, inplace=True)
    return df

def binning_popularity(df: pd.DataFrame):
    a = df["popularity"].quantile(0.25)
    b = df["popularity"].quantile(0.5)
    c = df["popularity"].quantile(0.75)
    df["A"] = 0
    df.loc[df["popularity"] >= a, "A"] = 1
    df.loc[df["popularity"] >= b, "A"] = 2
    df.loc[df["popularity"] >= c, "A"] = 3
    df = df.drop(["popularity"], axis=1)
    df.rename(columns={'A': 'popularity'}, inplace=True)
    return df

def binning_vote_average(df: pd.DataFrame):
    a = df["vote_average"].quantile(0.25)
    b = df["vote_average"].quantile(0.5)
    c = df["vote_average"].quantile(0.75)
    df["A"] = 0
    df.loc[df["vote_average"] >= a, "A"] = 1
    df.loc[df["vote_average"] >= b, "A"] = 2
    df.loc[df["vote_average"] >= c, "A"] = 3
    df = df.drop(["vote_average"], axis=1)
    df.rename(columns={'A': 'vote_average'}, inplace=True)
    return df

def binning_google_trend(df: pd.DataFrame):
    a = df["google_trend"].quantile(0.25)
    b = df["google_trend"].quantile(0.5)
    c = df["google_trend"].quantile(0.75)
    df["A"] = 0
    df.loc[df["google_trend"] >= a, "A"] = 1
    df.loc[df["google_trend"] >= b, "A"] = 2
    df.loc[df["google_trend"] >= c, "A"] = 3
    df = df.drop(["google_trend"], axis=1)
    df.rename(columns={'A': 'google_trend'}, inplace=True)
    return df

def cal_info_gain(df: pd.DataFrame):
    # information_gain
    p_gain = df["profitable"].value_counts(normalize=True)[1]
    p_loss = df["profitable"].value_counts(normalize=True)[0]
    entropy_profitable = -(p_gain * math.log2(p_gain) + p_loss * math.log2(p_loss))
    IG = {}
    # Calculate IG(*, profitable) = H(profitable) - conditional entropy
    for col_name in df.columns:
        if col_name == "profitable":
            continue
        col = df[col_name]
        # get the set of probabilities of values
        p_set = col.value_counts(normalize=True)
        condition_entropy_sum = 0
        for val in p_set.keys():
            col_conditional = df[col == val]["profitable"]
            p_set_conditional = col_conditional.value_counts(normalize=True)
            entropy_conditional = 0
            if 1 in p_set_conditional.keys():
                p_gain_conditional = p_set_conditional[1]
                entropy_conditional += p_gain_conditional * math.log2(p_gain_conditional)
            if 0 in p_set_conditional.keys():
                p_loss_conditional = p_set_conditional[0]
                entropy_conditional += p_loss_conditional * math.log2(p_loss_conditional)
            entropy_conditional *= -1
            condition_entropy_sum += p_set[val] * entropy_conditional
        IG[col_name] = entropy_profitable - condition_entropy_sum
    res = sorted(IG.items(), key=lambda x:x[1], reverse=True)
    # for feature, ig in res:
    #     print("IG(%s) = %.4f" % (feature, ig))
    labels, values = zip(*res)
    plt.figure(figsize=(6.4, 4.8))  
    plt.bar(labels, values, color='skyblue')
    plt.xticks(rotation=20, ha='right')
    plt.savefig('./figures/info_gain.pdf', format="pdf")
    plt.clf()
    return