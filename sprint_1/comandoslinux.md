### Comandos fundamentais Linux

sintaxe => COMANDO -OPCOES ARQUIVOS/DIRETORIOS^C

#### Movimentação entre repositórios (cd):
cd (ir para um repositório/pasta)<br>
cd .. (volta um repositório e posso concatenar também ../../.. <- voltaria 3 pastas)<br>
cd - (leva para o último diretório que estava)<br>
cd ~ (home do usuário)<br>
** pode-se usar o / para dar um "auto-complete" no nome do repositório caso voce nao saiba ele completamente
cd etc && ls<br>

ls (lista de arquivos ou conteúdo de um diretório)<br>
ls -ltr (atualização)<br>

cat <nome arquivo> (mostra o conteúdo de um arquivo)<br>
cat -n <nome> (mostra o conteúdo + linhas)<br>
<br>
touch <nome> (muda o horario da atualização mostrado no -ltr)<br>
touch <nome.formato> (criar aqruivos sem conteudo)<br>
<br>
man <comando> ex: man ls (man é o manual do comando, mostra todos parametros e derivações daquele comando)<br>

#### Gerenciamento de arquivos e diretórios:

mkdir <nome> (cria um novo repositório na pasta atual)<br>
mkdir -v <nome> (executa o comando detalhando o que está sendo feito)<br>
rm <nome.formato> (remoção de arquivos)<br>
rmdir <nome> (remove diretório)<br>
rmdir -p <nome>/<nome>/<nome> (remoção de uma cadeia de diretorios)<br>
cp <primeiro arquivo> <segundo arquivo> (copia conteudo de um arquivo)<br>
cp -r (copia as pastas dentro do diretorio para outro)<br>
cp <diretorio>/* <diretorio2> (copia todo diretorio para outro utilizando o /* cópia integral de arquivos)<br>
mv <nome.formato> (recorta o arquivo, parecido com o ctrl x do windows)<br>
mv <nome.fomrato> + local/ (move arquivos para dentro da pasta específica)<br>
pwd (mostra em qual diretório atual o terminal está)<br>

#### Gerenciamento de pacotes/aplicativos:

sudo (dá permissões, tipo o modo adm do windows)<br>
apt-get (atualiza ou instala um software)<br>

sudo apt-get update (atualiza todos os repositórios e pacotes instalados no sistema)<br>
sudo apt-get upgrade (atualiza os softwares)<br>
sudo apt-get install <aplicativo> (instala o aplicativo)<br>
sudo apt-get purge <aplicativo> (deleta o aplicativo)<br>
sudo apt-get autoremove (deleta pacotes/aplicativos desnecessários)<br>
apt-cache search <aplicativo> (pesquisa aplicativo especifico)<br>

**Alternativa para o apt-get é utilizar apenas apt:**<br>
sudo apt install <aplicativo> <br>
sudo apt update<br>
sudo apt autoremove<br>

#### Filtro e busca de arquivos e diretórios:

head <arquivo> (mostra o topo de um arquivo)<br>
head -n 1 <arquivo> (mostra a linha 1)<br>
tail <arquivo> (mostra o fim do arquivo)<br>
tail -f <arquivo> (mostra as atualizações/ debug de logs)<br>
grep 'palavra' <arquivo> (o mesmo que ctrl + f, pesquisa palavras especificas num arquivo)<br>
find -name 'arquivo' (procura diretorios/arquivo e mostra seu endereço)<br>
find -empty (mostra todos os diretorios vazios existentes no sistema)
find -name 'arquivo' -type f (arquivos)<br>
find -name 'arquivo -type d (diretorios)<br>
locate <arquivo> (mostra endereço de arquivos mais antigos)<br>

#### Editores de texto:
#### **Nano**
alt + a (seleciona área)<br>
alt + 6 (copiar)<br>
ctrl + u (cola)<br>
cltr + k (recorte)<br>
alt + / (movimenta para o fim do arquivo)<br>
alt + \ (movimenta para o topo do arquivo)<br>
alt + g (movimenta para linha especifica)<br>

#### **Vim**
:x (salva e fecha o arquivo)<br>
:w (salva o arquivo)<br>
:q (sai do arquivo)<br>
:q!(sai do arquivo sem intenção de salvar)<br>
d (deleta uma linha)<br>
u (refaz = ctrl Z do windows)<br>

#### Gerenciamento de usuários e grupos: 

sudo adduser <nome> (cria novo usuário)<br>
ls /home/ (mostra os usuários que está na máquina)
sudo userdel --remove <nome_usuario> (deleta usuario e tudo sobre ele)
sudo usermod -c 'novo_nome' <nome_usuario> (renomeia o nome do display do usuario)
sudo usermod -l novo_nome_usuario -d /home/novo_nome_usuario -m nome_usuario (renomeia nome e diretorio do usuario)
sudo usermod -L nome_usuario (bloqueia usuario)
sudo usermod -U nome_usuario (desbloqueia usuario)

getent group (visualiza todos os grupos existentes na máquina)
sudo groupadd + nome do grupo (cria novo grupo)
sudo groupdel + nome do grupo (remove grupo)
groups nome de usuario (mostra qual grupo o usuario pertence)
sudo usermod -a -G grupo + nome de usuario (move usuario para outro grupo)
sudo gpasswd -d nome do usuario + grupo (remove usuario de um grupo)
sudo su (transforma o usuario em super user e voce nao precisa mais pedir permissao com o "sudo")
exit (sai do modo super usuario)
passwd (muda senha do usuario)





