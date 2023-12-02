##### Produção dos Dados:
1. Dados primários:
- Coletados por quem faz a análise
- Confiáveis
- Possuem maior controle

**Desvantagens:
- Alto custo
- Demanda tempo
- Maior número de pessoas serão necessárias para obtenção

2. Dados secundários:
- Coletados por terceiros
- Não confiáveis
- Não possuem muito controle

**Desvantagens
- Falta de controle
- Dados inadequados
- Fontes não confiávies

##### Gráficos

* Representação de fenômenos
* Refletir padrões gerais
* Facilita a interpretação
* Resume informações

Evidenciam: 
- Tendências
- Ocorrências ocasionais
- Valores mínimos e máximos
- Ordens de grandezas dos fenômenos observados

Questionamentos importantes para implementação de uma representação gráfica
- Realmente seria a melhor opção utilizar um gráfico?
- Qual o meu público alvo?
- Qual a finalidade do meu gráfico?
- Que tipo de gráfico devo utilizar?
- Como apresentar o meu gráfico? (software)
- Dimensões ideias de um gráficos (escala, zoom, legendas, fontes...)

Bibliotecas de gráficos:
- Matplotlib `` import matplotlib.pyplot as plt
- Seaborn `` import seaborn as sns

Tipos de gráficos
1. Gráficos de barras:
- Servem para variáveis __qualitativas__;
- Formado por retângulos horizontais de larguras iguais;
- Possuem como objetivo: Comparar grandezas entre categorias; Categorias com designações extensas.
```
y = [1, 2, 3, 4, 5]
x = ['n1', 'n2', 'n3', 'n4', 'n5']
x2 = ['variável um', 'variável dois', 'variável três', 'variável quatro', 'variável cinco']

# Barra horizontal

plt.barh(x2, y, color='y')
plt.xlabel('Variável eixo X', size=15)
plt.ylabel('Categorias', size=15)
plt.title('Meu primeiro gráfico')
```
Resultado gerado:
![[Pasted image 20231201120228.png]]

2. Gráficos de colunas:
- Possui as mesmas propriedades que o gráfico horizontal, porém por estar na vertical, necessita de uma legenda de categorias um pouco menor com menos caracteres.
```

```
Resultado gerado:
![[Pasted image 20231201120253.png]]

3. Gráficos de setores(pizza):
- Utilizado quando queremos comparar o valor de uma categoria com relação ao total;
- Número pequeno de categorias.
Ex:
![[Pasted image 20231201120907.png]]

4. Gráficos de linhas

5. Histogramas