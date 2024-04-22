# encode genres
import ast
import pandas as pd

def encode_genres(df: pd.DataFrame):
    all_genres = set()
    df['genres'] = df['genres'].apply(ast.literal_eval)
    for genre_list in df["genres"]:
        for genre in genre_list:
            all_genres.add(genre)
    all_genres = list(all_genres)
    df[all_genres] = 0
    for i, genre_list in enumerate(df["genres"]):
        df.loc[i, genre_list] = 1
    df = df.drop(["genres"], axis=1)
    return df

def encode_production_companies(df: pd.DataFrame):
    # company_freq = {}
    # df['production_companies'] = df['production_companies'].apply(ast.literal_eval)
    # for company_list in df["production_companies"]:
    #     for company_id in company_list:
    #         if company_id not in company_freq:
    #             company_freq[company_id] = 0
    #         company_freq[company_id] += 1
    # company_freq = {x:y for x, y in company_freq.items() if y > 5}
    # df["company_freq"] = 0
    # for i, company_list in enumerate(df["production_companies"]):
    #     for id in company_list:
    #         if id in company_freq:
    #             df.loc[i, ["company_freq"]] = 1
    #             break
    df = df.drop(["production_companies"], axis=1)
    return df
