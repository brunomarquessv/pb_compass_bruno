import requests
import pandas as pd
import os
from dotenv import load_dotenv
from IPython.display import display

load_dotenv()
API_KEY= os.getenv("API_KEY")

# movie_id de Dunkirk
dunkirk_id = "374720"
# movie_id de Red Line
red_line_id = "8741"

# url base da api
base_url = "https://api.themoviedb.org/3/movie/"

# adiciona o movie_id para a url
url_dunkirk = f"{base_url}{dunkirk_id}?api_key={API_KEY}&language=pt-BR"
url_red_line = f"{base_url}{red_line_id}?api_key={API_KEY}&language=pt-BR"

# faz a solicitação por meio da url
response_dunkirk = requests.get(url_dunkirk)
response_red_line = requests.get(url_red_line)

# converte para .json
data_dunkirk = response_dunkirk.json()
data_red_line = response_red_line.json()

# obtem os dados dos filmes
filme_dunkirk = data_dunkirk
filme_red_line = data_red_line

# print dos dados dos filmes
print("\n 1º Filme")
print("\nTitle:", filme_dunkirk['title'])
print("Release Date:", filme_dunkirk['release_date'])
print("Overview:", filme_dunkirk['overview'])
print("Vote Count:", filme_dunkirk['vote_count'])
print("Vote Average:", filme_dunkirk['vote_average'])

print("\n 2º Filme")
print("\nTitle:", filme_red_line['title'])
print("Release Date:", filme_red_line['release_date'])
print("Overview:", filme_red_line['overview'])
print("Vote Count:", filme_red_line['vote_count'])
print("Vote Average:", filme_red_line['vote_average'])
