# Introdução as tecnologias essenciais da AWS

## O que é computação em nuvem?

**Computação em nuvem é a entrega de recursos de TI sob demanda pela Internet com pagamento conforme o uso.

[What is cloud computing?](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/what-is-cloud-computing.html)

#### Benefícios:
- Agilidade
- Elasticidade
- Economia de custo
- Implantação global

## Infraestrutura global da AWS

A infraestrutura da amazon, tem alcance global e está localizada em pontos chaves e isolados em várias regiões do mundo. Este isolamento, permite que os serviços sejam mais tolerantes a falhas e tenham maior estabilidade. 

[Infraestrutura global](https://aws.amazon.com/pt/about-aws/global-infrastructure/)
[Regiões e zonas de disponibilidade](https://aws.amazon.com/pt/about-aws/global-infrastructure/regions_az/)

## Tecnologias essenciais

#### Computação:
- Desenvolvimento, implantação, execução e dimensionamento de aplicações e cargas de trabalho na AWS Cloud

**Serviços:**
1. **Amazon Elastic Compute Cloud (EC2) - Instâncias(máquinas virtuais):**
- É um serviço da web que disponibiliza capacidade computacional segura e redimensionável na nuvem.

2. **Amazon EC2 Auto Scaling:** 
- Aumente ou reduza o número de instâncias

3. **Elastic Load Balancing:**
- Distribuição do tráfego de entrada

4. **Amazon Elastic Container Service - contêineres:**
- Execução de aplicações em clusters gerenciados

5. **Amazon Elastic Kubernetes Service:**
- Execução de aplicações Kubernetes na AWS e no local

6. **AWS Lambda:**
- Execução de códigos em resposta a eventos, sem a utilização de servidores

**Benefícios:
1. **Elasticidade:** permite que que os clientes aumentem ou diminuam a capacidade computacional em minutos. 
2. **Controle:** os clientes possuem controle total sobre as instâncias implantadas, incluindo acesso a raiz ou de administrador, além da possibilidade de interações.
3. **Flexibilidade:** grande variedade instâncias, sistemas operacionais (SO) e pacotes de software.
4. **Integrado:** é integrado a maioria dos serviços da aws, ofertando uma solução completa em computação.
5. **Confiabilidade:** possibilita uma alta disponibilidade, no qual a substituição de instâncias pode ser rápida e previamente encomendadas.
6. **Segurança:** toda a arquitetura de rede dos serviços, são feitos para satisfazer as necessidades das empresas com as maiores exigências e diretrizes de segurança.
7. **Econômico:** os clientes pagam por uma taxa pequena 

#### Armazenamento: 

**Serviços de armazenamento:**
1. Amazon Elastic Block Store (EBS)
- Armazenamento persistente em nível de bloco - funciona como um disco rígido para instancias EC2.
![[amazon_ebs.png]]

2. Amazon Simple Storage Service (S3)
- Armazenamento de objetos durável e dimensionável.
![[Pasted image 20231223182820.png]]
![[Pasted image 20231223182835.png]]

3. Amazon S3 Glacier (S3 Glacier)
- Arquivamento e backup de dados.

4. AWS Storage Gateway
- Integre armazenamento na nuvem com cargas de trabalho no local.

5. Amazon Elastic File System (EFS)
- Armazenamento de arquivos para instâncias do Amazon EC2.

6. Amazon FSx
- Armazenamento de arquivos para sistemas de arquivos amplamente usados.

#### Banco de Dados:

**Serviços de banco de dados:**
1. Amazon RDS
- Capacidade econômica e redimensionável

2. Amazon DynamoDB
- Bancos de Dados NoSQL com alto desempenho e previsível

3. Amazon ElastiCache
- Recuperação rápida e gerenciada de informações

![[Pasted image 20231223183452.png]]

#### Redes: 

**Serviços de redes:**
1. Amazon VPC
Rede virtual na nuvem
![[Pasted image 20231223184358.png]]
![[Pasted image 20231223184520.png]]
2. Security Groups
Controle ao acesso de instâncias

3. NACL (Listas de controle de acesso de rede)
Controle do acesso às sub-redes

4. Amazon Route 53
Direcionamento de usuários finais para aplicativos da internet

#### Segurança

**Serviços de segurança:**
1. Proteção de infraestrutura -
2. Identity and Access Management (IAM) - gerenciamento de acesso de usuários e grupos 
3. Detecção -
4. Proteção de dados - 
5. Resposta a incidentes -
6. Conformidade - 

Resumo:
![[Pasted image 20231223185435.png]]


## Serviços e Soluções

#### Estratégia de migração:

**Os sete Rs**
1. Re-hospedar: lift and shift
- Recriação de rede on-premises, hospedada somente na AWS
- Automatização com ferramentas como o AWS Application Migration Service
- Maior facilidade de otimização e de reprojetar aplicativos após migração
1. Redefinir plataforma
2. Realocar
3. Refatorar
4. Retirar
- Desativação de aplicativos inúteis
- Que reduzem a velocidade, o gerenciamento e a segurança
5. Reter/Revisitar
- Manter determinados aplicativos on-premises
6. Recomprar
- Mover fluxos de trabalho para software como serviço (SaaS)

#### Práticas recomendadas de arquitetura na nuvem

1. Design à prova de falhas e nada vai falhar
2. Segurança em cada camada
3. Utilizar diferentes opções de armazenamento
4. Implementar a elasticidade
5. Pensar paralelo
6. O acoplamento fraco liberta você
7. Não temer restrições

**AWS Well-Architected Framework

É um conjunto de melhores práticas e princípios recomendados para criar e implantar arquiteturas de nuvem eficientes, seguras e resilientes. 

Ele fornece orientações sobre como projetar sistemas na AWS com foco em seis pilares principais:

1. Excelência operacional
2. Segurança
3. Confiabilidade
4. Eficiência de desempenho
5. Otimização de custos
6. Sustentabilidade

**Exemplo de: otimização de custos
- Dimensionamento correto de instâncias
- Aumento da elasticidade do aplicativo
- Escolha do modelo correto de preço
- Otimização do armazenamento

[Well-Architected](https://aws.amazon.com/pt/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc)

**Estrutura de adoção da nuvem AWS:**
- AWS Cloud Adoption Framework

| Recursos de negócios | Recursos técnicos|
| ---------------------| -----------------|
| Negócios             | Plataforma       |
| Pessoas              | Segurança        |
| Governança           | Operações        |
