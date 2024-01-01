# Introdução a soluções de avaliação de dados

##### Definições: 
- **Avaliação** é um exame detalhado de algo para entender sua natureza ou determinar suas características essenciais 
- **Avaliação de dados** é o processo de compilar, processar e analisar dados para que você possa usá-los para tomar decisões (processo analítico específico sendo aplicado). 
- **Análise** é a avaliação sistemática dos dados

##### Benefícios da Análise de Dados em grande escala:
1. Personalização do cliente
2. Detecção de fraudes
3. Detecção de ameaças à segurança
4. Comportamento do usuário
5. Modelagens e previsões financeiras
6. Alerta em tempo real

Soluções **eficazes** de avaliação de dados exigem armazenamento e capacidade de avaliação de dados **praticamente em** **tempo real**, com **baixa latência**, gerando **retornos de alto valor**.

##### Componentes de uma solução de avaliação de dados

Dados brutos >> Ingerir e coletar >> Armazenar >> Processar Analisar >> Consumir Visualizar >> Respostas e informações 

1. Coletar - Montar dados de várias fontes
2. Armazenar - Armazena dados em repositórios
3. Processamento - Manipulação dos dados nas formas necessárias
4. Consumo - Onde os dados são apresentados nos formatos necessários 

##### Desafios de uma solução de avaliação de dados

"Os 5 V's do Big Data"

1. Volume: é a quantidade de dados que serão ingeridos pela solução ou, o tamanho total dos dados que ingressam. 
2. Velocidade: rapidez com que os dados entram em uma solução.
3. Variedade: número de fontes e tipos de fontes diferentes que a solução usará.
4. Veracidade: grau de precisão, exatidão e confiabilidade dos dados.
5. Valor: capacidade de uma soluçao de extrair informações significativas dos dados armazenados e analisados.

##### O que é necessário avaliar para a primeira etapa do planejamento?

**Conhecer a origem dos dados:** que podem surgir desde banco de dados e armazenamento de arquivos on-premises, dados de streaming (dados de negócios), quanto de conjunto de dados públicos (dados de censo, saúde, populacional...)

**Conhecer as opções para processas esses dados:** cobrindo toda a fase de processamento dos dados, desde a fase de ingestão/coleta até a fase de consumo.

**Saber o que aprender com os dados:** em outras palavras, aprender a ler os dados.

## Volume: armazenamento de dados

Quando as empresas têm **mais dados** do que conseguem **processar** e **analisar**, a empresa possui um problema em **volumes de dados**.

##### Classificações da origem dos dados 

- **Dados estruturados:** são organizados e armazenados na forma de valores que são agrupados em linhas e colunas de uma tabela (relacional).
- **Dados semiestruturados:** são armazenados em conjuntos de pares de chave-valor que são agrupados em elementos em um arquivo (não relacional).
- **Dados não estruturados:** não são estruturados de forma consistente. Alguns dados pode ter uma estrutura semelhante a dados semiestruturados, mas outros podem conter apenas metadados. 

##### Amazon Simple Storage Service (S3)

S3 é uma plataforma de armazenamento de objetos (arquivos) tanto estruturado, quanto não estruturados.

**Objetos:**  são compostos por um arquivo e quaisquer metadados que descrevam esse arquivo.
**Buckets:** são contêineres lógicos para objetos. Você pode ter um ou mais buckets em sua conta e controlar o acesso a cada um individualmente.

**Os benefícios do Amazon S3 são:**  
- Armazenamento de qualquer coisa;
- Armazenamento seguro de objetos;
- Acesso HTTP nativamente on-line;
- Escalabilidade ilimitada;
- Durabilidade de ~99,9%

**Amazon S3 como uma solução de armazenamento:**

1. **Desacoplar o armazenamento do processamento:** Você pode ter buckets separados para os dados brutos, resultados de processamento temporários e resultados finais.
2. **Paralelização:** você pode acessar qualquer um desses locais de armazenamento de um processo, em paralelo, sem afetar negativamente os outros processos.
3. **Arquitetura de dados centralizada:** O Amazon S3 facilita a criação de um ambiente multi-tenant em que muitos usuários podem trazer suas próprias ferramentas de análise de dados para um conjunto comum de dados.
4. **Integração com serviços AWS sem cluster e sem servidor:** O Amazon S3 também se integra à computação sem servidor do AWS Lambda para executar código sem provisionar ou gerenciar servidores.
5. **Interfaces de programação de aplicativos (APIs) padronizadas:**  

##### Data lake 
**Repositório centralizado** que permite armazenar dados **estruturados**, **semiestruturados** e **não estruturados** em qualquer escala.

Benefícios de um data lake na AWS:
- Armazenamento de dados econômica
- Segurança e conformidade
- Diferentes ferramentas de coleta e ingestão
- Categorização e gerenciamento de dados
- Transformação de dados em informações significativas 

##### Armazenamento de dados estruturados

**Data warehouse:** é um repositório central de dados estruturados provenientes de muitas origens de dados.

![[Pasted image 20231228140714.png]]
![[Pasted image 20231228141108.png]]

**Data marts:**
![[Pasted image 20231228141023.png]]

**Solução em data warehouse na AWS**

- **Amazon Redshift:** é um serviço de data warehousing que permite configurar e implementar um novo data warehouse, que armazena e consulta conjuntos de dados em grande escala.

- **Apache Hadoop:** framework de código aberto, que auxilia no armazenamento e processamento de dados, oferecendo suporte a transferências rápidas de dados, aumentando assim o processamento para consultar complexas. 

Benefícios do Hadoop:
1. Lida melhor com as incertezas: facilita a navegação de dados, descoberta e avaliação única de dados. 
2. Gerencia variedade de dados: processa dados estruturado, semiestruturados e nao estruturados. Incluindo praticamente, qualquer formato de dados existentes. 
3. Ampla seleção de soluções: 
4. Visa ao volume e a velocidade: graças a arquitetura distribuida, os clusters podem processar enormes quantidades de dados de maneira econômica.

## Velocidade: processamento de dados 

Quando as empresas precisam de **informações rápidas dos dados**, mas os sistemas presentes não conseguem atender a este tipo de necessidade, há um problema de **velocidade.**

**Processamento de dados:** refere-se a coleta e a manipulação dos dados para produzir informações significativas. A coleta dos dados são divididas em coleta de dados (obtenção de dados de várias fontes para armazenar e avaliar uma única origem) e processamento de dados (formatação, organização e controle de dados). 

Variação na velocidade dos dados: 
- Processamento em batch: Grandes intermitências de dados
1. Periódico
2. Programado 

- Processamento em stream: Pequenas intermitências de dados
1. Quase em tempo real (minutos)
2. Em tempo real (milissegundos)

![[Pasted image 20231228153326.png]]

##### Processamento em batch
O _**processamento em batch**_ é a execução de uma série de programas ou _trabalhos_ em um ou mais computadores sem intervenção manual.

![[Pasted image 20231228154204.png]]

**Arquitetura de um processamento em batch** 
Serviços/Tecnologias AWS que são utilizadas: 

- Amazon S3 -  um serviço de armazenamento de objetos que oferece escalabilidade, disponibilidade de dados, segurança e desempenho líderes do setor.
- AWS Lambda - serviço que permite executar código sem provisionar ou gerenciar servidores
- Amazon EMR - serviço que fornece um framework Hadoop gerenciado que torna fácil, rápido e econômico processar grandes quantidades de dados em instâncias do Amazon EC2.
- AWS Glue - serviço de extração, transformação e carregamento (ETL) totalmente gerenciado que facilita a preparação e carregamento de dados para análise.
- Amazon Redshift - é um datawarehouse rápido que torna simples e econômica a análise de todos os seus dados nos data warehouses e data lakes.


##### Processamento em stream

**Amazon Kinesis** 
- Amazon Kinesis Data Firehose - capturar, transformar e carregar streams de dados em datastores da AWS para análises quase em tempo real usando ferramentas existentes de business intelligence.
-  Amazon Kinesis Data Streams - criar aplicativos personalizados e em tempo real para processar streams de dados usando frameworks comuns de processamento de streams.
- Amazon Kinesis Video Streams - facilita o streaming seguro de vídeos a partir de dispositivos conectados à AWS, onde podem ser usados para análise, machine learning (ML) e outros processamentos.
- Amazon Kinesis Data Analytics - processar streams de dados em tempo real com SQL ou Java sem precisar aprender novas linguagens de programação ou frameworks de processamento.

**Arquitetura de um processamento stream**
Serviços/Tecnologias AWS que são utilizadas: 

- Amazon Kinesis 
- Amazon S3 
- **Amazon Athena** - serviço de consultas interativas que facilita a análise de dados no Amazon S3 usando o SQL padrão. O Athena é sem servidor, portanto, não há infraestrutura para gerenciar e você paga apenas pelas consultas executadas.
- **Amazon Quicksight** - um serviço de business intelligence (BI) rápido e desenvolvido para a nuvem que facilita o fornecimento de informações a todos em sua organização (visualização dos dados).


## Variedade: estruturas e tipos de dados

Quando sua empresa fica **sobrecarregada** pelo **grande número de origens dos dados** para analisar e você **não consegue encontrar sistemas** para fazer a análise, sabe que tem um problema de **variedade**.

**Tipos de dados:** 
![[Pasted image 20231228174735.png]]
Dados semiestruturados: 
- Armazenados como elementos e atributos
- Banco de dados NoSQL ou não relacional
- Nenhum esquema predefinido
- Podem ser armazenados em arquivos
- Altamente flexível
![[Pasted image 20231228174749.png]]

Dados não estruturados:
- Armazenados como arquivos
- Nenhum esquema predefinido
- Arquivos em PDF e CSV

![[Pasted image 20231228175433.png]]

##### Banco de dados estruturados

![[Pasted image 20231228180532.png]]
![[Pasted image 20231228180608.png]]
![[Pasted image 20231228180654.png]]

##### Banco de dados semiestruturados e não estruturados

- Banco de dados não relacionais 
São criados para armazenar e gerenciar dados semiestruturados e não estruturados de forma que oferaça rápida coleta e recuperação. 

1. Armazenamento de documentos
- Tipo de banco de dados não relacional
- Armazena dados semiestruturados e não estruturados 
- Variedade de formatos
- Flexibilidade 
- Fácil dimensionamento

2. Armazenamento de chave-valor 
- Tipo de banco de dados não relacional
- Armazena dados não estruturados em formato chave-valor
- Armazenados em uma única tabela
- Alta flexibilidade
- Lida com uma grande variedade de tipos de dados

**Amazon DynamoDB:** é o serviço aws referente a banco de dados não relacionais de documentos e chave-valor que fornece grande desempenho. O serviço é gerenciado em váris regiões e conta com recursos integrados de segurança, backup e restauração. 

## Veracidade: limpeza e transformação

Quando se tem dados que **não são controlados**, provenientes de vários **sistemas diferentes** e **não consegue fazer curadoria dos dados** de maneiras significativas, você sabe que tem um problema de **veracidade**.

- ***Curadoria*** é a ação ou o processo de selecionar, organizar e ciudar de itens em uma coleção.
- ***Integridade dos dados*** é a manutenção e a garantia de precisão e consistência dos dados durante todo seu ciclo de vida. 
- ***Veracidade dos dados*** é o grau em que os dados são exatos, precisos e confiáveis.

##### Integridade dos dados

Garantia de que os dados são confiáveis.

**Ciclo de vida dos dados:** 
1. Criação:  auditorias de software
2. Agregação:  
3. Armazenamento 
4. Acesso 
5. Compartilhamento 
6. Arquivamento. 

**Algumas definições:**

- **Limpeza de dados:** é o processo de detecção e correção de corrupções nos dados.
- **Integridade referencial:** é o processo para garantir que as restrições das relações da tabela sejam impostas.
- **Integridade do domínio:** é o processo para garantir que os dados inseridos em um campo correspondam ao tipo de dados definido para esse campo.
- **Integridade da entidade:** é o processo para garantir que os valores armazenados em um campo correspondam às restrições definidas para esse campo.

- **Esquema de banco de dados:** é um esquema de defesa, utilizado para organizar objetos e impor restrições de integridade, como relacionamentos.
- **Esquemas lógicos:** Os esquemas lógicos se concentram nas restrições a serem aplicadas aos dados no banco de dados. Isso inclui a organização de tabelas, visualizações e verificações de integridade.
- **Esquemas físicos:** Os esquemas físicos se concentram no armazenamento real de dados em disco ou em um repositório de nuvem. Esses esquemas têm detalhes sobre os arquivos, índices, tabelas particionadas, clusters e muito mais.

**Práticas de identificação de problemas de integridade dos dados**

- Qual o tipo de limpeza
- De onde os erros vêm
- Quais são as alterações aceitáveis
- Os dados originais têm valor?

###### Consistência do banco de dados

_**ACID** é um acrônimo para **A**tomicidade, **C**onsistência, **I**solamento e **D**urabilidade. É um método para manter a consistência e a integridade em um banco de dados estruturado._

_**BASE** é um acrônimo para **BA**sicamente disponível, e**S**tado flexível, **E**ventualmente consistente. _É um método para manter a consistência e a integridade em um banco de dados estruturado ou semiestruturado.__

##### Processo de ETL
Extração, transformação e carregamento (ETL) é o processo de coletar dados de origens brutas e transformá-los em um tipo comum.


## Valor: relatórios e business intelligence

Quando há **grandes volumes** de **dados** usados para corroborar **algumas informações valiosas**, você pode estar perdendo o **valor** dos seus dados.

##### Análise de dados
- Análise de informações: é o processo de análise de informações para encontrar o valor contido nelas.
- Análise operacional: se concentra nas operações digitais de uma organização (recuperar, analisar e relatar dados para as operações de TI).

Tipos de análises:
1. Descritiva (mineração de dados): o que aconteceu?
	Se concentra em informações.
2. Diagnóstica: por que aconteceu?
	Se concentrando em retrospectiva e informações.
3. Preditiva: o que acontecerá?
	Se concentra em informações e previsões.
4. Prescritiva: o que deveria ter sido feito?
	 Se concentra na previsão.
	- Geração de informações
	- Suporte a decisões
	- Automação de decisões utilizando algoritmos em machine learning
1. Cognitiva e artificial: o que deve ser feito?
	Se concentra na previsão e na entrada de uma hipótese
	- Automação de decisões por meio de algoritmos em deep learning

**Serviços analíticos e velocidade**

Velocidade dos diferentes tipos de processamento: 
- Análise em batch: **A análise em batch** geralmente envolve consulta a grandes quantidades de dados “frios”.
- Análise Interativa: **Análise interativa** normalmente envolve a execução de consultas intrincadas em conjuntos de dados complexos em altas velocidades.
- Análise em stream: **Análise em stream** exige a ingestão de uma sequência de dados e a atualização incremental de métricas, relatórios e estatísticas de resumo em resposta a cada registro de dados recebido.

###### Visualização de dados

**Preparação de dados**
Processos que os dados passam, para confirmar seu valor:

- Exploração de dados
- Limpeza de dados
- Transformação de dados
- Visualização de dados - esse é o processo de criação de ***relatórios*** e painéis para apresentar o valor contido nos dados.

**Relatórios analíticos**

Tipos de relatórios: 
- Estáticos: são encontrados em formato PDF e powerpoint, são facilmente encontrados na web.
- Interativos: 
- Painéis:
