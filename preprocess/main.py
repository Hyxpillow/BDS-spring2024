import pandas as pd
from label import generate_label
from encoding import encode_genres, encode_production_companies
from feature_selection import select_genres_by_info_gain
from feature_selection import select_companies_by_info_gain
from data_fusion import merge_google_trend
from normalization import normalize

df = pd.read_csv("./download/raw.csv")
df = df[["budget", "revenue", "runtime", "year", "release_date", "genres", "vote_average", "popularity", "production_companies"]]
df["budget"] = df["budget"].astype(int)
df["runtime"] = df["runtime"].astype(int)

df = generate_label(df) #
df = encode_genres(df) #
df = select_genres_by_info_gain(df) #
df = encode_production_companies(df)
df = select_companies_by_info_gain(df)
df = merge_google_trend(df) #
df.to_csv("./preprocess/clean_norm_free.csv", index=False)
df = normalize(df) #
df.to_csv("./preprocess/clean.csv", index=False)
