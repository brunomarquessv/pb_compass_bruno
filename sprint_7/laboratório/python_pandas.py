import pandas as pd

df = pd.read_csv(
    r"C:\Users\bruno\dev\pb_compass_bruno\sprint_7\laboratório\actors.csv"
    )
# 1. Identifique o ator com maior número de filmes e a quantidade de filmes:
maior_numero_filmes = df.loc[df["Number of Movies"].idxmax()]
ator_maior_numero_filmes = maior_numero_filmes['Actor']
numero_filmes = maior_numero_filmes['Number of Movies']

# Saída -> O ator com maior número de filmes é o Robert DeNiro que realizou um total de 79 filmes
print(f"\nO ator com maior número de filmes é o {ator_maior_numero_filmes} que realizou um total de {numero_filmes} filmes")

# 2. Média da coluna que contém o maior número de filmes
media_filmes = df["Number of Movies"].mean()

#Saída -> A média do número de filmes é de 37.88
print(f"\nA média do número de filmes é de {media_filmes:.2f}")

# 3. Ator/atriz com a maior média por filme
maior_media_filmes = df.loc[df["Average per Movie"].idxmax()]
ator_maior_numero_filmes = maior_media_filmes["Actor"]
media_filmes_ator = maior_media_filmes["Average per Movie"]

#Saída -> O artista com maior média por filme é o Anthony Daniels com uma média de 451.8
print(f"\nO artista com maior média por filme é o {ator_maior_numero_filmes} com uma média de {media_filmes_ator}")

# 4. Filmes mais frequentes e sua respectiva frequência
filmes_mais_frequentes = df["#1 Movie"].mode()
frequencia_filmes_mais_frequentes =df["#1 Movie"].value_counts().max()

#Saída -> O filme mais frequente é o The Avengers com uma frequência de 6 vezes
print(f"\nO filme mais frequente é o {', '.join(filmes_mais_frequentes)} com uma frequência de {frequencia_filmes_mais_frequentes} vezes")



