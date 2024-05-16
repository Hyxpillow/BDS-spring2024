# There are 15 columns for genres after encoding, which may lead to
# curse of dimensionality
import math
from matplotlib import pyplot as plt
import pandas as pd

def select_genres_by_info_gain(df: pd.DataFrame, topK = 2):
    all_genres = ['Science Fiction', 'Fantasy', 'Horror', 'War', 
                  'Family', 'Drama', 'Documentary', 'Western', 
                  'Comedy', 'Music', 'History', 'Mystery', 
                  'Animation', 'Romance', 'Action', 'Crime', 
                  'Thriller', 'Adventure']
    p_loss = df["profitable"].value_counts(normalize=True)[0]
    p_profit = df["profitable"].value_counts(normalize=True)[1]
    entropy_profitable = -(p_profit * math.log2(p_profit) + 
                           p_loss * math.log2(p_loss))
    info_gain = {}
    for genre in all_genres:
        p_true = df[genre].value_counts(normalize=True)[1]
        tmp = df[df[genre] == 1]["profitable"].value_counts(normalize=True)
        cond1_entropy = 0
        if 1 in tmp.keys():
            cond1_entropy -= tmp[1] * math.log2(tmp[1])
        if 0 in tmp.keys():
            cond1_entropy -= tmp[0] * math.log2(tmp[0])

        p_false = df[genre].value_counts(normalize=True)[0]
        tmp = df[df[genre] == 0]["profitable"].value_counts(normalize=True)
        cond2_entropy = 0
        if 1 in tmp.keys():
            cond2_entropy -= tmp[1] * math.log2(tmp[1])
        if 0 in tmp.keys():
            cond2_entropy -= tmp[0] * math.log2(tmp[0])

        info_gain[genre] = entropy_profitable - (p_true * cond1_entropy + p_false * cond2_entropy)
    
    res = sorted(info_gain.items(), key=lambda x:x[1], reverse=True)
    x = [item[0] for item in res]
    y = [item[1] for item in res]
    for item in res:
        print(item[0], item[1])
    # plt.bar(x, y)
    # plt.xlabel('Genres')
    # plt.ylabel('Infomation Gain')
    # plt.show()

    topk_genres = [genre for genre, _ in res[:topK]]
    # Compared with the results from RapidMiner, the procedure here is correct.
    drop_genres = [genre for genre in all_genres if genre not in topk_genres]
    df = df.drop(drop_genres, axis=1)
    return df

def select_companies_by_info_gain(df: pd.DataFrame):
    return df