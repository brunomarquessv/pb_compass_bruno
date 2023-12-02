* __Funções de primeira classe:__ Capacidade de usar as funções como entidades de primeira classe, em variáveis. Elas podem ser também: 
1. Atribuídas a variáveis;
2. Passadas como argumentos para outras funções;
3. Retornecidas de outras funções;
4. Armazenadas em coleções;
5. Manipuladas por expressões;

* __Funções de Alta Ordem:__ Capacidade de uma função de receber como parâmetro e/ou retornar outras funções.

* __Closure:__ Funções que podem ser aninhadas e ter acesso ao escopo da função na qual foi definida, inclusive impedindo o Garbage Colector de libera-las. exemplo:
```
def multiplier(x):
	def calc(y):
		return x * y
	return calc


if __name__ = '__main__':
	dobro = multiplier(2)
	triplo = multiplier(3)

	print(dobro, triplo)

	print(f'O triplo de 3 é {triplo(3)}')
	print(f'O dobro de 7 é {dobro(7)}')
	print(f'O dobro de 3 é {dobro(3)}')
```
* __Funções anônimas(lambda):__

* __Map:__

* __Filter:__

* __Reduce:__