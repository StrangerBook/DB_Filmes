# DB_Filmes

## Definição do sistema
O código é feito para uma empresa que desejar fazer um site de lista de filmes que é guardado num banco de dados, sendo esse codigo a parte dos funcionarios de adicionar filmes, deletar filmes, alterar filmes e ler os dados do banco de dados.

## Implementação do código
O código possui integração com MySQL onde é possivel criar instâncias com id, nome e sinopse na tabela "filmes" do banco de dados, ver todos os filmes registrados na própria, pesquisar um filme por nome ou id, alterar o dado de qualquer filme registrado (achando
ele por id ou por nome também) e por ultimo deletar um filme apenas por id (para evitar confusões e não apagar algum filme sem querer). Todas ações descritas precisam de comfirmação para que não sejam feitas alterações sem querer no banco de dados.

## Como usar
Para o uso correto do codigo é necessario ter o "Visual Studio Code" (VSCode), o "MySQL Workbench" e o "MySQL 8.0 Comand Line Client"
Para baixar os MySQL's: entre site do MySQL -> Downloads -> MySQL Community (GPL) Downloads » -> MySQL Installer for Windows e escolher a versão que quiser, abrindo o instalador clique no "+" antes de "MySQL Servers" -> clique no "+" antes de "MySQL Server" ->
clique no "+" antes de "MySQL Server 8.0" e escolha a ultima versão (8.0.41 no momento) -> clique na seta verde no meio da tela, siga em frente até ele pedir para criar uma senha (ou colocar a que já existe), salve essa senha e siga até instalar o servidor.
Após a instalação do servidor, abra novamente o instalado, clique em "Add ..." na direita da tela -> clique no "+" antes de "Applications" -> clique no "+" antes de "MySQL Workbench" -> clique no "+" antes de "MySQL Workbench 8.0"
escolha a ultima versão e siga em frente.
Para o VSCode bas entrar no site no próprio e procurar pelos dowloads.

Com isso instalado abra a barra de pesquisa do windows e pesquise por "MySQL 8.0 Comand Line Client" ao abrir, coloque a senha que você anotou na instalação. Abra a barra de pesquisa novamente e pesquise por "MySQL Workbench 8.0 CE" ao abrir clique no "+" na frente
de "MySQL Connections" escolha um nome para a conexão e clique "ok", depois clique na conexão que você criou, dentro do bloco de texto no meio do aplicativo coloque os comandos dentro do arquivo "BancoDados.sql" e clique no botão com apenas um raio.
Dentro do "VSCode" abra um terminal e digite "pip install mysql-connector-python" e envie.

Após isso, nas primeiras linhas de código Python, mude os numeros dentro as aspas da linha que contém ' password ="123456" ' para a senha que você anotou.

Enfim o código está pronto para uso e totalmente integrado com o banco de dados!
