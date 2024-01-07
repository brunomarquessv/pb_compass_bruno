# Lab AWS Lambda

## Passo a passo do laboratório

1. Criando a função lambda 
![](../lab%20aws%20lambda/assets/Screenshot%202024-01-07%20141105.png)
<br>
<br>
<br>
2. Criando a imagem do pandas no docker para implementar na Layer(camada)
![](../lab%20aws%20lambda/assets/Screenshot%202024-01-07%20132422.png)

2.1 Buildando a imagem do docker
![](../lab%20aws%20lambda/assets/Screenshot%202024-01-07%20132603.png)

2.2 Acessando shell do container para construir a estrutura de diretórios
![](../lab%20aws%20lambda/assets/Screenshot%202024-01-07%20132718.png)

2.3 Instalando o pandas no conteiner
![](../lab%20aws%20lambda/assets/Screenshot%202024-01-07%20132803.png)

2.4 Zipando os arquivos do layer com as bibliotecas instaladas para implementar no bucket s3

![](../lab%20aws%20lambda/assets/Screenshot%202024-01-07%20132901.png)
![](../lab%20aws%20lambda/assets/Screenshot%202024-01-07%20133147.png)
![](../lab%20aws%20lambda/assets/Screenshot%202024-01-07%20133154.png)

2.4.1 Upload do zip dentro do bucket
![](../lab%20aws%20lambda/assets/Screenshot%202024-01-07%20133421.png)
![](../lab%20aws%20lambda/assets/Screenshot%202024-01-07%20133429.png)

3. Criando a camada e implementando a ela a imagem da biblioteca panda 
![](../lab%20aws%20lambda/assets/Screenshot%202024-01-07%20133557.png)

3.1 Adicionando a camada a função lambda
![](../lab%20aws%20lambda/assets/Screenshot%202024-01-07%20133654.png)

4. Aumentando o timeout e memoria da lambda e executando o script com sucesso!
![](../lab%20aws%20lambda/assets/Screenshot%202024-01-07%20141115.png)
![](../lab%20aws%20lambda/assets/Screenshot%202024-01-07%20140756.png)
![](../lab%20aws%20lambda/assets/Screenshot%202024-01-07%20140804.png)