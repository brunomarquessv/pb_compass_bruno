***E1
```sql
select *
from livro
where publicacao > '2015-01-01'
order by cod
```

***E2
```sql
select titulo, 
       valor
from livro
order by valor desc
limit 10
```

***E3
```sql
select count(codeditora) as quantidade, 
        nome, 
        estado, 
        cidade

from editora as editora
left join livro as livro
    on livro.editora = editora.codeditora
left join endereco as endereco
    on endereco.codendereco = editora.endereco
where titulo is not null
group by nome
order by nome
```

***E4
```sql
select nome, 
       codautor,
       nascimento,  
       count(livro.autor) as quantidade
from autor as autor
left join livro as livro
    on livro.autor = autor.codautor
group by nome
order by nome
```

***E5
```sql
select  autor.nome
from autor 
left join livro
    on livro.autor = autor.codautor
left join editora 
    on editora.codeditora = livro.editora
left join endereco 
    on endereco.codendereco = editora.endereco
where endereco.estado <> 'PARANÁ'
group by autor.nome
```

***E6
```sql
select codautor, 
       nome, 
       count(*) as quantidade_publicacoes
from autor as autor
left join livro as livro
    on autor.codautor = livro.autor
group by nome
having quantidade_publicacoes = 
        (select max(quantidade_publicacoes) 
        from (select count(*) as quantidade_publicacoes 
        from livro 
        group by autor) as quantidade_publicacoes)
order by codautor
```

***E7
```sql
select nome
from autor as autor
left join livro as livro
    on livro.autor = autor.codautor
where livro.autor is null
order by nome
```
