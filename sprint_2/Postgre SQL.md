##### Comandos básicos:

* select -> seleciona colunas na tabela;
*sintaxe: select coluna_1, coluna_2, coluna_3

* from -> "de" destina o local que a tabela selecionado pelo *select* está;
*sintaxe: from sales.customers

* distinct -> remove as linha as linhas duplicadas e mostra apenas as linhas distintas;
*sintaxe: select distinct coluna_1

* where -> filtra linhas de acordo com uma condição;
*sintaxe: where condição_x = true // where state = 'PE' 

* order by -> ordenar por...
*sintaxe: order by age // obs: numeral ja é filtrado em forma crescente como padrão e ao utilizar 'desc' (sem aspas) ele filtra por ordem decrescente

* limit -> limita o número de linhas da tabela que será mostrado
*sintaxe: limit 10

##### Operadores:
<u>Operadores de comparação</u>:
padrão de todas as outras linguagens ***( '| |' possui a mesma ideia de && em Java)

<u><b>Operadores lógicos: </b></u>
-- (1) Usados para unir expressões simples em uma composta
-- (2) AND: Verifica se duas comparações são simultaneamente verdadeiras
-- (3) OR: Verifica se uma ou outra comparação é verdadeiras
-- (4) BETWEEN: Verifica quais valores estão dentro do range definido
-- (5) IN: Funciona como multiplos OR (cria um conjunto)
-- (6) LIKE e ILIKE: Comparam textos e são sempre utilizados em conjunto com o 
-- operador %, que funciona como um coringa, indicando que qualquer texto pode 
-- aparecer no lugar do campo
-- (7) ILIKE ignora se o campo tem letras maiúsculas ou minúsculas na comparação
-- (8) IS NULL: Verifica se o campo é nulo

##### Funções agregadas:

