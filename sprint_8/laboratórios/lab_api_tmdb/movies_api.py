import requests
import pandas as pd
import os
from dotenv import load_dotenv
from IPython.display import display

load_dotenv()
API_KEY= os.getenv("API_KEY")

# movie_id de 1917
movie_id_1917 = "530915"
# movie_id do pearl harbor
movie_id_pearl_harbor = "676"

# url base da api
base_url = "https://api.themoviedb.org/3/movie/"

# adiciona o movie_id para a url
url_1917 = f"{base_url}{movie_id_1917}?api_key={API_KEY}&language=pt-BR"
url_pearl_harbor = f"{base_url}{movie_id_pearl_harbor}?api_key={API_KEY}&language=pt-BR"

# faz a solicitação por meio da url
response_1917 = requests.get(url_1917)
response_pearl_harbor = requests.get(url_pearl_harbor)

# converte para .json
data_1917 = response_1917.json()
data_pearl_harbor = response_pearl_harbor.json()

# obtem os dados dos filmes
filme_1917 = data_1917
filme_pearl_harbor = data_pearl_harbor

# print dos dados dos filmes
print("\n 1º Filme")
print("\nTitle:", filme_1917['title'])
print("Release Date:", filme_1917['release_date'])
print("Overview:", filme_1917['overview'])
print("Vote Count:", filme_1917['vote_count'])
print("Vote Average:", filme_1917['vote_average'])

print("\n 2º Filme")
print("\nTitle:", filme_pearl_harbor['title'])
print("Release Date:", filme_pearl_harbor['release_date'])
print("Overview:", filme_pearl_harbor['overview'])
print("Vote Count:", filme_pearl_harbor['vote_count'])
print("Vote Average:", filme_pearl_harbor['vote_average'])
