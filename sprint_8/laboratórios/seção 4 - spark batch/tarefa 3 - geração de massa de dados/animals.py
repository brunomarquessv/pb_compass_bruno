import csv

animals = [
            "Mico-leão-dourado", "Arara-azul-de-lear", "Sagui-de-tufos-brancos", "Tamanduá-mirim", "Tatu-bola", 
           "Jabuti-piranga", "Macaco-prego", "Arara-vermelha", "Jandaia-verdadeira", "Tatu-canastra", 
           "Quati", "Capivara", "Anta", "Sabiá-laranjeira", "Siriema", "Tamanduá-bandeira", "Pica-pau-amarelo", 
           "Veado-catingueiro", "Bicho-preguiça", "Gato-do-mato"
           ]



ordened_animals = sorted(animals)

print("Animais em ordem crescente:")
[print(animal) for animal in ordened_animals]

with open("animais.csv", "w", newline="") as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    for animal in ordened_animals:
        escritor_csv.writerow([animal])
