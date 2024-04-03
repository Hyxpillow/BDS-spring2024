import calendar
import json
import os
import tqdm
import requests
import datetime

out_dir = "dataset/"

def generate_date_ranges(start_year, end_year):
    date_ranges = []
    for year in range(start_year, end_year):
        for month in range(1, 13):
            start_date = datetime.date(year, month, 1)
            _, last_day = calendar.monthrange(year, month)
            end_date = start_date.replace(day=last_day)
            date_ranges.append((start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")))
    return date_ranges

    return None

def get_movie_list(begin_date, end_date):  # return dict
    url = "https://api.themoviedb.org/3/discover/movie"
    headers = {"accept": "application/json",}
    params = {
        "api_key": "feb8f97f3769e0912538c6999b2a6b30",
        "primary_release_date.gte": begin_date,
        "primary_release_date.lte": end_date,
        "page": "1",
    }
    response = requests.get(url, headers=headers, params=params)
    json_data = response.json()

    total_pages = json_data["total_pages"]
    print("downloading", begin_date, end_date, total_pages)
    id_list = []
    for page in tqdm.tqdm(range(total_pages)):
        page += 1
        params = {
            "api_key": "feb8f97f3769e0912538c6999b2a6b30",
            "primary_release_date.gte": begin_date,
            "primary_release_date.lte": end_date,
            "page": str(page),
        }
        response = requests.get(url, headers=headers, params=params)
        json_data = response.json()
        for movie_dict in json_data["results"]:
            id_list.append(movie_dict["id"])
    return id_list

def get_movie_detail(id):
    url = "https://api.themoviedb.org/3/movie/" + str(id)
    headers = {"accept": "application/json"}
    params = {"api_key": "feb8f97f3769e0912538c6999b2a6b30"}
    response = requests.get(url, headers=headers, params=params)
    json_data = response.json()
    with open(out_dir + str(id) + ".json", "w") as f:
        json.dump(json_data, f, indent=4)

movie_list = []
if not os.path.exists("movie_list.txt"):
    date_ranges = generate_date_ranges(2021, 2024)
    for begin_date, end_date in date_ranges:
        movie_list_period = get_movie_list(begin_date, end_date)
        movie_list += movie_list_period
    with open("movie_list.txt", "w") as f:
        for id in movie_list:
            f.write(str(id)+'\n')
else:
    with open("movie_list.txt", "r") as f:
        for line in f:
            movie_list.append(int(line))

for i, id in enumerate(movie_list):
    if not os.path.exists(out_dir + str(id) + ".json"):
        movie_list = movie_list[i:]
        break
    
for id in tqdm.tqdm(movie_list):
    get_movie_detail(id)
    
