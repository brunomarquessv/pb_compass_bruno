### Permissões Linux

leitura (r - read)<br>
escrita (w - write)<br>
execução (x - execute)<br>

**Entendendo as permissões**

***1 222 333 444***

1: diretório ou arquivo<br>
222: permissões do owner (dono)<br>
333: permissões do grupo (que o arquivo pertence)<br>
444: permissões dos demais usuários (que não são donos do arquivo e também não fazem parte do grupo do arquivo)

**Exemplo**
***drwxr-xr-x***
<-> 1 222 333 444
1 serve para d ou -: diretório(d) ou arquivo(-)
d: directory 
r: read
w: write
x: execute
-: não há permissão

drw-rw-r--: diretório, owner e grupo com permissão de ler e escrever, demais só com permissão de ler
-r--r--r--: arquivo, só a permissão de leitura para todos

### Gerenciamento básico de Redes

**Como a web funciona?**
1. Envio de requisição para um domínio (DNS)
2. Verificação do domínio (dns = ip)
3. Requisição da resposta para o servidor que pertence a este domínio
4. Retorno da resposta a quem solicitou

**O que é DNS**
DNS = Domain Name System
* Traduz o endereço de IP em um domínio, para que não precisassemos gravar números de IP.

Funcionamento: 

1. Uma pessoa digita um domínio no navegador;
2. Um servidor lê o DNS digita; (DNS Resolver);
3. Encontra o servidor pela combinação de DNS e IP;
4. Retorna ao usuário o site desejado.

**Portas** 

* É um endpoint (outro domínio que poderemos acessar do mesmo site) e sempre estará associado a um IP

Exemplos:
* 20: FTP
* 22: SSH
* 80: HTTP
* 443: HTTPS

**TCP**

* Transmission Control Protocol = TCP
* Protocolo utilizado para transmissão de dados pela rede 

Onde é aplicado:

* SMTP (envio de emails);
* FTP (transferência de arquivos);
* HTTP (protocolo para navegar pela internet).

**UDP**

* User Datagram Protocol = UDP;
* Serve para envio de dados pela rede ;
* O UDP se preocupa mais com a velocidade de envio do que com a confiabilidade;
* TCP se torna mais seguro e UDP mais rápido;
* UDP é muito utilizado em jogos online e streams.







