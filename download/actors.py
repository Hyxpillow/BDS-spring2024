import datetime
import pandas as pd
import requests
from tqdm import tqdm

def calculate_years_since(date_str):
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    today = datetime.date.today()
    years = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
    return years

def get_actor_info(actor_name):
    url = "https://api.themoviedb.org/3/search/person"
    headers = {"accept": "application/json"}
    params = {"api_key": "feb8f97f3769e0912538c6999b2a6b30",
              "query": actor_name}
    response = requests.get(url, headers=headers, params=params)
    json_dict = response.json()
    res_list = json_dict["results"]
    if len(res_list) == 0:
        return 0, 0
    actor_id = res_list[0]["id"]
    url = "https://api.themoviedb.org/3/person/"+str(actor_id)
    headers = {"accept": "application/json"}
    params = {"api_key": "feb8f97f3769e0912538c6999b2a6b30"}
    response = requests.get(url, headers=headers, params=params)
    json_dict = response.json()
    birthday = json_dict["birthday"]
    if birthday != None:
        years_since = calculate_years_since(birthday)
    else:
        years_since = 0
    popularity = json_dict["popularity"]
    return years_since, popularity
    

df = pd.read_csv("download/raw.csv")
df["actors"] = "[]"
for i, movie_title in enumerate(tqdm(df["title"])):
    url = "http://www.omdbapi.com/"
    headers = {"accept": "application/json"}
    params = {"apikey": "273cd79a",
              "t": movie_title}
    response = requests.get(url, headers=headers, params=params)
    json_dict = response.json()
    if "Actors" in json_dict:
        actor_list = json_dict["Actors"].split(", ")
        df.loc[i, ["actors"]] = str(actor_list)
        core_actor = 0
        avg_age = 0
        for actor_name in actor_list:
            age, popularity = get_actor_info(actor_name)
            core_actor = max(popularity, core_actor)
            avg_age += age
        avg_age /= len(actor_list)
        df.loc[i, ["core_actor"]] = int(core_actor)
        df.loc[i, ["actor_avg_age"]] = int(avg_age)
df.to_csv("download/raw.csv", index=False)