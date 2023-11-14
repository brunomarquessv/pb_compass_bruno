#sql 
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
* Usados para unir expressões simples em uma composta
* AND: Verifica se duas comparações são simultaneamente verdadeiras
* OR: Verifica se uma ou outra comparação é verdadeiras
* BETWEEN: Verifica quais valores estão dentro do range definido
* IN: Funciona como multiplos OR (cria um conjunto)
* LIKE e ILIKE: Comparam textos e são sempre utilizados em conjunto com o 
-- operador %, que funciona como um coringa, indicando que qualquer texto pode 
-- aparecer no lugar do campo
* ILIKE ignora se o campo tem letras maiúsculas ou minúsculas na comparação
* IS NULL: Verifica se o campo é nulo

##### Funções agregadas:
* Servem para executar operações aritmética nos registros de uma coluna 
* Funções agregadas não computam células vazias (NULL) como zero
* Na função COUNT() pode-se utilizar o asterisco (*) para contar os registros
* COUNT(DISTINCT ) irá contar apenas os valores exclusivos

Tipos de Join:
left join, inner join, right join e full join

* Servem para combinar colunas de uma ou mais tabelas
* Pode-se chamar todas as colunas com o asterisco (*), mas não é recomendado
* É uma boa prática criar aliases para nomear as tabelas utilizadas 
* O JOIN sozinho funciona como INNER JOIN

Union:
* union -- unir o conteúdo de duas tabelas (obs: não será unido conteúdos que contenham em ambas as tabelas)
* union all -- unir todo o conteúdo de duas tabelas (obs: une também caso haja conteúdo repetidos entre ambas as tabelas)

Subquerys:


##### Tratamento de Dados:
<u>Conversão de unidades:</u>
* Texto para números usa-se o operador ": :"

***ex: select '2021-10-01' :: date - '2021-02-01'::date
ex: select '100'::numeric - '80'::numeric

Função ***cast( )
ex: select cast('2020-01-01' as date) - cast('2021-02-04' as date)

<u>Tratamento Geral:</u>
case when
coalesce

<u>Tratamento de texto:</u>
lower 
upper
trim
replace

<u>Tratamento de data/hora:</u>
interval
date_trunc
extract
datediff

<u>Funções:</u>
Criar função: ***create function


##### Manipulação de tabelas:
<u>Tabelas - Criação e deleção:</u>
* Para criar tabelas a partir de uma query basta escrever a query normalmente e
colocar o comando INTO antes do FROM informando o schema e o nome da tabela 
a ser criada: 
***ex.: select customer_id, 
      ((current_date - birth_date) / 365) as idade_cliente
      into temp_table.customers_age
from sales.customers

* Para criar tabelas a partir do zero é necessário (a) criar uma tabela vazia 
com o comando CREATE TABLE (b) Informar que valores serão inseridos com o comando
***INSERT INTO seguido do nome das colunas (c) Inserir os valores manualmente em forma 
de lista após o comando VALUES:
***ex.: 
select distinct professional_status
from sales.customers

***create table temp_tables.profissoes (
	professional_status varchar,
	status_profissional varchar
)

***insert into temp_tables.profissoes
(professional_status, status_profissional)

***values
('freelancer', 'freelancer'),
('retired', 'aposentado(a)'),
('clt', 'clt'),
('self_employed', 'autônomo(a)'),
('other', 'outro'),
('businessman', 'empresário(a)'),
('civil_servant', 'funcionário público(a)'),
('student', 'estudante')

* Para deletar uma tabela utiliza-se o comando DROP TABLE
***ex.: drop table temp_tables.profissoes

<u>Linhas - inserção, atualização e deleção:</u>

* Para inserir linhas em uma tabela é necessário (a) Informar que valores serão 
inseridos com o comando INSERT INTO seguido do nome da tabela e nome das colunas 
(b) Inserir os valores manualmente em forma de lista após o comando VALUES
* Para atualizar as linhas de uma tabela é necessário (a) Informar qual tabela
será atualizada com o comando UPDATE (b) Informar qual o novo valor com o comando SET 
(c) Delimitar qual linha será modificada utilizando o filtro WHERE
* Para deletar linhas de uma tabela é necessário (a) Informar de qual tabela as
linhas serão deletadas com o comando DELETE FROM (b) Delimitar qual linha será 
deletada utilizando o filtro WHERE



