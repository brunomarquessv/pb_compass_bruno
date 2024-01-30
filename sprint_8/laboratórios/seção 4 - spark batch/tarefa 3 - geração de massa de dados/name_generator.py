import random
import time
import os
import names

#semente de aleatoriedade
random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# gerar os nomes aleatórios
print("Gerando nomes aleatórios...")

aux = []
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

start_time = time.time()  # marcar o tempo de início

dados = []
for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

end_time = time.time()  # marcar o tempo de fim

# gerador de arquivo de texto contendo todos os nomes, um a cada linha
nome_arquivo = "nomes_aleatorios.txt"
with open(nome_arquivo, "w") as file:
    for nome in dados:
        file.write(nome + "\n")

tempo_execucao = end_time - start_time
print("arquivo '{}' gerado com sucesso.".format(nome_arquivo))
print("tempo de execução: {:.2f} segundos".format(tempo_execucao))