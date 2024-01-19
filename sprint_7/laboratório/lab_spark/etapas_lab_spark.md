## Apache Spark - Contador de Palavras

- Como não consegui tirar print de tudo que eu tinha feito, pois houve inúmeras tentativas, vou informar o passo a passo
de como foi resolvido o laboratório 

1. Foi realizado o pull da imagem dentro do ambiente docker 
2. Foi criado um conteiner a partir da imagem com o comando: docker run -it -p 8888:8888 jupyter/all-spark-notebook
3. Como tudo foi feito dentro uma distro WSL criada por mim, especificamente para fazer o exercício, com o wget peguei 
o readme.md que estava dentro do meu diretório utilizando wget + link do raw. 
4. Fiz a cópia do arquivo README.md do /home/linux para a /home/ do docker ->
docker cp /home/linux/pasta/"README.md" id-container:/home/ <br>
**Na quarta etapa, foi onde tive mais problemas, pois houve inúmeras tentativas de copiar o arquivo README.md que estava
na home do meu linux, para a home do meu conteiner docker**
5. Após conseguir fazer a cópia do arquivo README.md iniciei o pyspark dentro do docker pelo comando 
docker exec -it id-container pyspark
![](../lab_spark/assets/Screenshot%202024-01-18%20203807.png)
6. Realizei os scripts para concluir a atividades, segue imagem com os scripts:
![](../lab_spark/assets/Screenshot%202024-01-18%20203503.png)
