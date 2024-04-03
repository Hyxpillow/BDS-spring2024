import os
import json
import pandas as pd
from tqdm import tqdm

dataset_dir = "./dataset/"
json_name_list = os.listdir(dataset_dir)
json_list = []
for json_name in tqdm(json_name_list):
    with open(dataset_dir + json_name, "r") as f:
        json_dict = json.load(f)
        if "genres" in json_dict:
            json_dict["genres"] = [genre_dict["name"] for genre_dict in json_dict["genres"]]
        else:
            json_dict["genres"] = []
        json_list.append(json_dict)
# features_list = ["budget", "genres", "overview", "release_date", 
#                  "revenue", "runtime", "title","vote_average", "vote_count"]
features_list = ["id","budget", "release_date", "revenue", "runtime","vote_average", "vote_count", "year", "month", "genres", "overview"]
df = pd.DataFrame(json_list)
df = df[df["budget"] > 0]
df = df[df["revenue"] > 0]
df = df[df["runtime"] >= 60]
for feature in df:
    if feature not in features_list:
        df = df.drop([feature], axis=1)
df["release_date"] = pd.to_datetime(df["release_date"])
df["year"] = df["release_date"].dt.year
df["month"] = df["release_date"].dt.month
df = df[features_list]
df = df.drop(["release_date"], axis=1)
df.to_csv("dataset.csv", index=False)
