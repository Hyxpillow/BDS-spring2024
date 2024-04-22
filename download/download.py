import threading
import pandas as pd
import requests
import calendar
import tqdm
import datetime

def generate_date_ranges(start_year, end_year):
    date_ranges = []
    for year in range(start_year, end_year):
        for month in range(1, 13):
            start_date = datetime.date(year, month, 1)
            _, last_day = calendar.monthrange(year, month)
            end_date = start_date.replace(day=last_day)
            date_ranges.append((start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")))
    return date_ranges

def get_movie_list(begin_date, end_date, thread_buffer):  # return dict
    url = "https://api.themoviedb.org/3/discover/movie"
    headers = {"accept": "application/json",}
    params = {
        "api_key": "feb8f97f3769e0912538c6999b2a6b30",
        "primary_release_date.gte": begin_date,
        "primary_release_date.lte": end_date,
        "with_runtime.gte": 60,
        "vote_count.gte": 10,
        "with_original_language": "en",
        "page": "1",
    }
    response = requests.get(url, headers=headers, params=params)
    json_data = response.json()

    total_pages = json_data["total_pages"]
    print("downloading", begin_date, end_date, total_pages)
    id_list = []
    for page in range(total_pages):
        page += 1
        params = {
            "api_key": "feb8f97f3769e0912538c6999b2a6b30",
            "primary_release_date.gte": begin_date,
            "primary_release_date.lte": end_date,
            "with_runtime.gte": 60,
            "vote_count.gte": 10,
            "with_original_language": "en",
            "page": str(page),
        }
        response = requests.get(url, headers=headers, params=params)
        json_data = response.json()
        for movie_dict in json_data["results"]:
            id_list.append(movie_dict["id"])
    thread_buffer.append(id_list)
    print("complete", begin_date, end_date, total_pages)


date_ranges = generate_date_ranges(2020, 2024)
thread_buffer = []
thread_list = []
for begin_date, end_date in date_ranges:
    t = threading.Thread(target=get_movie_list, args=(begin_date, end_date, thread_buffer,), daemon=True)
    thread_list.append(t)
for t in thread_list:
    t.start()
for t in thread_list:
    t.join()
movie_list = [id for batch in thread_buffer for id in batch]

json_list = []
for id in tqdm.tqdm(movie_list):
    url = "https://api.themoviedb.org/3/movie/" + str(id)
    headers = {"accept": "application/json"}
    params = {"api_key": "feb8f97f3769e0912538c6999b2a6b30"}
    response = requests.get(url, headers=headers, params=params)
    json_dict = response.json()
    if "genres" in json_dict:
        json_dict["genres"] = [genre_dict["name"] for genre_dict in json_dict["genres"]]
    else:
        json_dict["genres"] = []
    if "production_companies" in json_dict:
        json_dict["production_companies"] = [company_dict["id"] for company_dict in json_dict["production_companies"]]
    else:
        json_dict["production_companies"] = []
    json_list.append(json_dict)

features_list = ["id","title","budget", "release_date", "revenue", "runtime","vote_average", "vote_count","popularity", "genres", "production_companies", "overview"]
df = pd.DataFrame(json_list)
df = df[df["budget"] > 100000]
df = df[df["revenue"] > 0]
df = df[features_list]
df["release_date"] = pd.to_datetime(df["release_date"])
df["year"] = df["release_date"].dt.year
df["month"] = df["release_date"].dt.month
df.to_csv("./download/raw.csv", index=False)