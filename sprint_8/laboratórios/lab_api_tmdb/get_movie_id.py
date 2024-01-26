import requests
from movies_api import API_KEY

# função para obter o movie_id com base no título do filme
# de acordo com a documentação do tdmb
def get_movie_id(movie_title):
    search_endpoint = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": API_KEY, "query": movie_title}
    response = requests.get(search_endpoint, params=params)
    data = response.json()

    if response.status_code == 200 and data["results"]:
        return data["results"][0]["id"]
    else:
        return None

pearl_harbor_id = get_movie_id("Pearl Harbor")
print("pearl harbor:", pearl_harbor_id)

_1917_id = get_movie_id("1917")
print("1917:", _1917_id)
