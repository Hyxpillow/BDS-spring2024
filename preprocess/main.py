import pandas as pd
from label import generate_label
from encoding import encode_genres, encode_production_companies
from feature_selection import select_genres_by_info_gain
from feature_selection import select_companies_by_info_gain
from data_fusion import merge_google_trend
from binning import binning, cal_info_gain
from normalization import normalize, cal_cov_matrix
from reduction import reduction
from statistic import statistic

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
# statistic(df)

df.to_csv("./datasets/clean_raw.csv", index=False)
df_bin = binning(df) #
df_bin = normalize(df_bin) #
cal_info_gain(df_bin)
df = normalize(df) #
cal_cov_matrix(df)

df.to_csv("./datasets/clean.csv", index=False)
df_bin.to_csv("./datasets/clean_binning.csv", index=False)

df = reduction(df)
df.to_csv("./datasets/clean_reduction.csv", index=False)
