### Comandos Fundamentais Git

**git init** (criação de um novo repositório/projeto)<br>
**git status** (confere o status do projeto, incluindo todas as alterações feitas nele)<br>
**mkdir <nome_da_pasta>** (criar pasta)<br>
**cd <nome_da_pasta>** (redireciona para dentro da pasta do projeto)<br>
**git add <nome arquivo> (adiciona arquivos novos a um projeto)<br>
**git add .** (adiciona todos os novos arquivos ao projeto)<br>
**git commit -m (message)** (comenta uma alteração)<br>
**git commit -a (all) -m** (comenta todos os arquivos que precisam de um commit)<br>
**git push** (envia o código para o repositório remoto)<br>
**git pull** (o comando busca por atualizações e ao ser encontradas, “puxa” para unir ao arquivo ou código atual já existente na máquina)<br>
**git clone <endereço>** (baixa um repositório de um servidor remoto “clonar repositório”) – lembrar-se de passar a referência do repositório remoto<br>
**git rm <arquivo.formato>** (deleta o arquivo da monitorização do git, ou seja, o arquivo continua existindo porém se forem feitas alterações no arquivo, não constará no git status) lembrar-se de dar um git commit<br>
**git log** (acessa o histórico de alterações recebendo uma informação de todos os commits realizados no projeto até o momento)<br>
**git mv <nome do arquivo> <endereço novo>** (renomear arquivo ou até mesmo move-lo para outra pasta. Excluindo o antigo arquivo e fazendo com que o novo seja monitorado pelo git)<br>
**git mv <local do arquivo/nome.formato> <local do arquivo/novo nome.formato>** (renomea o arquivo pelo git mv)<br>
**git checkout** (o arquivo modificado por ser retonardo ao estado original)<br>
**.gitignore** (arquivo utilizado para "falar" ao git para ignorar determinado arquivo ou até mesmo pastas utilizando o sufixo /*)<br>
**git reset** (podemos resetar as mudanças feitas, geralmente utilizado com a flag --hard. todas as alterações de commitadas e também as pendentes serão excluídas)<br>

### Branches

**git branch <nome>** (comando utilizado para se criar uma nova branch)<br>
**git branch** (lista todos os branchs existentes no projeto)<br>
**git branch -d / --delete <nome do branch>** (deleta o branch e geralmente se utiliza o --delete quando o branch foi criado errado)<br>
**git checkout <nome branch>** (utilizado para alternar entre diferentes branches ou revisões (commmits))<br>
**git checkout -b <nome nova branch>** (utilizado para criação de um novo branch e ao mesmo tempo alternar entre ele)<br>
**git merge <nome>** (une o codigo de dois branchs distintos "une as branches")<br>
**git stash** (outro metodo para salvar as modificações atuais para prosseguir com outra abordagem de solução e não perder o código obs: após o comando o branch será resetado para a sua versão de acordo com o repo)<br>
**git stash list** (verificar as stashs já criadas do projeto)<br>
**git stash apply <nº stash>** (recuperar stash)<br>
**git stash show -p <nº stash>** (mostra quais foram as alterações feitas naquela stash)<br>
**git stash clear** (deleta todas as stashs do projeto)<br>
**git stash drop <numero>** (deleta stash especifica do projeto)<br>
**git tag -a <nome> -m "<msg>"** (cria tags nos branches e serve como checkpoint de um branch (demarcar estágios de um projeto))<br>
**git show <nome>** (comando para verificar existencia das tags)<br>
**git checkout <nome>** (igual podemos trocar de branch, podemos trocar de tag)<br>
**git push origin <nome>** (enviar o tag para o repositório de código)<br>
**git push origin --tags** (envia várias tags)<br>

### Compartilhamento e atualização

**git fetch** (mapeamento de branches e tags que ainda não foram reconhecidos)<br>
**git remote** (adiciona o repo para trackear ou remover)<br>
**git remote add origin <link>** (vincula repositório remoto ao git)<br>
**git submodule add <repo>** (adiciona submódulo (2 projetos em um mesmo repositório))<br>
**git submodule** (verificação de submodulos existentes)<br>
**git push --recurse-submodules=on-demand** (envia atualizações para o submodulo)<br>

### Análise e inspeção de repositórios

**git diff** (exibe a diferença de uma branch)<br>
**git diff <arquivo> <arquivo_b>** (exibe a diferença entre dois arquivos)<br>
**git shortlog** (nos dá um log resumido do projeto (cada commit será unido por nome de autor, sendo assim, poderemos ver quais commits foram enviados ao projeto e por quem))<br>

### Administração de repositórios

**git clean** (verifica e limpa os arquivos não trackeados, todos que não foram usados o "git add")<br>
**git gc** "garbage collector (limpa arquivos que não necessários para o projeto (melhora de performance))<br>
**git reflog** (é um git log mais completo, mapeia todos os passos do repositório (limite de 30 dias))<br>
**git archive --format zip --output master_files.zip main** (parecido com o gitclone - transforma o repositório em arquivo)
