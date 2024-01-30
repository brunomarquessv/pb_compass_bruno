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

dunkirk_id = get_movie_id("Dunkirk")
print("dunkirk:", dunkirk_id)

red_line_id = get_movie_id("Além da Linha Vermelha")
print("alem_da_linha_vermelha:", red_line_id)
