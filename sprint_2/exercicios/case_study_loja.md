***E8
```sql
select tbvendedor.cdvdd, 
        tbvendedor.nmvdd
        
from tbvendedor
left join tbvendas
    on tbvendedor.cdvdd = tbvendas.cdvdd
where tbvendas.status = 'Concluído'
order by tbvendas.status
limit 1
```

***E9
```sql
select cdpro, 
	   nmpro
from tbvendas
where status = 'Concluído' 
	and dtven between '2014-02-03' and '2018-02-02'
group by nmpro
limit 1
```

***E10
```sql
select tbvendedor.nmvdd as vendedor,
        SUM(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas,
        ROUND((SUM(tbvendas.qtd * tbvendas.vrunt) * tbvendedor.perccomissao / 100), 2) as comissao
        
from tbvendedor
left join tbvendas 
     on tbvendedor.cdvdd = tbvendas.cdvdd
where tbvendas.status = 'Concluído'
group by tbvendedor.cdvdd, 
         tbvendedor.nmvdd, 
         tbvendedor.perccomissao
order by comissao DESC;
```

***E11
```sql
select cdcli, 
       nmcli,
       sum(qtd*vrunt) as gasto
       
from tbvendas 
where status = 'Concluído'
group by cdcli, nmcli
order by gasto desc
limit 1;
```

***E12
```sql
SELECT
    d.cddep,
    d.nmdep,
    d.dtnasc,
    COALESCE(SUM(v.vrunt * v.qtd), 0) AS valor_total_vendas
FROM
    tbdependente d
INNER JOIN
    tbvendas v ON d.cdvdd = v.cdvdd
INNER JOIN (
    SELECT
        ve.cdvdd,
        COALESCE(SUM(vv.vrunt * vv.qtd), 0) AS valor_total_vendas_vendedor
    FROM
        tbvendas vv
    INNER JOIN
        tbvendedor ve ON vv.cdvdd = ve.cdvdd
    WHERE
        vv.status = 'Concluído' AND vv.vrunt > 0
    GROUP BY
        ve.cdvdd
    ORDER BY
        valor_total_vendas_vendedor ASC
    LIMIT 1
) AS vendedor_menor_valor ON 1 = 1  
WHERE
    v.status = 'Concluído'
GROUP BY
    d.cddep, d.nmdep, d.dtnasc
ORDER BY 
    valor_total_vendas
LIMIT 1;
```

***E13
```sql
select cdpro, 
       nmcanalvendas, 
       nmpro, 
       sum(qtd) as quantidade_vendas
from tbvendas
where tbvendas.status = 'Concluído'
group by nmcanalvendas, cdpro
order by quantidade_vendas
limit 10;
```

***E14
```sql
select estado, 
      round(avg(qtd*vrunt), 2) as gastomedio
from tbvendas
where status = 'Concluído'
group by estado
order by gastomedio desc
```

***E15
```sql
select cdven
from tbvendas
where deletado > 0
```

***E16
```sql
select estado, 
       nmpro,
       round(avg(qtd), 4) as quantidade_media
from tbvendas
where status = 'Concluído'
group by estado, nmpro
order by estado, nmpro
```

