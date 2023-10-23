### Comandos Fundamentais Git

git init(criação de um novo repositório/projeto)
<br>
git status (confere o status do projeto, incluindo todas as alterações feitas nele);
<br>
mkdir <nome_da_pasta> (criar pasta);
<br>
cd <nome_da_pasta> (redireciona para dentro da pasta do projeto);
<br>
git add <nome arquivo> (adiciona arquivos novos a um projeto);
<br>
git add . (adiciona todos os novos arquivos ao projeto);
<br>
git commit -m (message) (comenta uma alteração);
<br>
git commit -a (all) -m (comenta todos os arquivos que precisam de um commit);
<br>
git push (envia o código para o repositório remoto);
<br>
git pull (o comando busca por atualizações e ao ser encontradas, “puxa” para unir ao arquivo ou código atual já existente na máquina);
<br>
git clone <endereço> (baixa um repositório de um servidor remoto “clonar repositório”) – lembrar-se de passar a referência do repositório remoto;
<br>
git rm <arquivo.formato> (deleta o arquivo da monitorização do git, ou seja, o arquivo continua existindo porém se forem feitas alterações no arquivo, não constará no git status) lembrar-se de dar um git commit;
<br> 
git log (acessa o histórico de alterações recebendo uma informação de todos os commits realizados no projeto até o momento);
<br>
git mv <nome do arquivo> <endereço novo> (renomear arquivo ou até mesmo move-lo para outra pasta. Excluindo o antigo arquivo e fazendo com que o novo seja monitorado pelo git);
<br>
git mv <local do arquivo/nome.formato> <local do arquivo/novo nome.formato> (renomea o arquivo pelo git mv);
<br>
git checkout (o arquivo modificado por ser retonardo ao estado original);
<br>
.gitignore (arquivo utilizado para "falar" ao git para ignorar determinado arquivo ou até mesmo pastas utilizando o sufixo /*);
<br>
git reset (podemos resetar as mudanças feitas, geralmente utilizado com a flag --hard. todas as alterações de commitadas e também as pendentes serão excluídas);

## Branches

