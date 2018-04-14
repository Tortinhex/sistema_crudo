# Sistema de Papelaria

## Trabalho acadêmico feito em python com o framework flask

<br>

### 1. Instalação
* Instalar o [Python](https://www.python.org/downloads/) na versão 3.x (OBS: Na instalação, escolha a opção "instalação avançada" e selecione todos os checkbox disponíveis. Além disso, defina o local de instalação no C:/)
* Clonar o projeto em uma pasta (preferencialmente no C:/) com o comando <br>
`git clone https://github.com/Tortinhex/sistema_crudo.git` <br>
* Dentro da pasta do projeto, instale o ambiente virtual com o comando <br>
`pip install virtualenv`
* Criar o ambiente virtual com o comando <br>
`virtualenv env -p C:/Python36-32/python.exe` OBS: Veja no C:/ da maquina o nome da pasta de instalação do python
* Inicializar o ambiente virtual com o comando <br>
`env/Scripts/activate`
* Instalar as dependencias com o comando <br>
`pip install -r requirements.txt`
* Executar o projeto com o comando <br>
`python run.py runserver`


### 2. Documentação
* Flask `http://flask.pocoo.org/`
* Flask-sqlalchemy `http://flask-sqlalchemy.pocoo.org`
* Flask-migrate `https://flask-migrate.readthedocs.io`
* Flask-wtf `https://flask-wtf.readthedocs.io`
* Twitter Bootstrap `https://getbootstrap.com/`
* URL do projeto no heroku ``https://sis-papelaria-crd.herokuapp.com/provider


### 3. Funcionamento
Quando o comando `python run.py runserver` é executado, o motor do flask entra em execução e passa a "ouvir" as requisições HTTP baseadas no http://path-site/[controller]/[feature] (vide a documentação do Flask para maiores detalhes). Com excessão do controller index (/), todos os outros controllers podem ser acessados através da pasta ./app/constrollers/. Então, cada controller possui uma feature, onde as básicas são: <i>index, create, update e delete</i> e sempre retornam um HTML que podem ser acessados através da pasta ./app/templates/[controller]/[nome-pagina-html]. 
<br> 
Os formulários presentes no HTML são uma referência do objeto que podem ser acessado em ./app/forms/ e neste objeto são definidos os validadores, o tamanho do campo, nome do campo, placeholder e todos os outros parâmetros (vide o Flask-WTF para maiores detalhes) 
<br>
Por ser uma aplicação orientada ao objeto, o controller faz uso dos objetos para preencher a página. Os objetos podem ser acessados na pasta ./app/models/ e o relacionamento já construído pode ser acessado no arquivo papelaria-schema.png (OBS: Também existe o XML do esquema que pode ser aberto pela aplicação https://www.draw.io/).
<br>
Quando se modifica um objeto, este será sincronizado na base de dados de acordo com as configurações definidas nele. Para maiores detalhes, veja a documentação do Flask-sqlalchemy
<br>
Sempre que um objeto for modificado, deve-se executar o comando `python run.py db upgrade` para sincronizar a base de dados. Caso houver erros, é possível deletar a base de dados (storage.db), deletar a pasta migrations e executar os comando `python run.py db init`, `python run.py db migrate` e `python run.py db upgrade`. Desta forma, a base será refeita. Para maiores detalhes, veja a documentação do Flask-migrate
<br>
Para a estilização das páginas, foi usado o framework Bootstrap (https://getbootstrap.com/) e este arquivo pode ser acessado em ./app/static/css/ e ./app/static/js/. Além disso, existe o arquivo ./app/static/css/styles.css que serve para otimizar o css caso desejável.

### 4. Ciclo da aplicação

Para exemplificar, segue abaixo o fluxo que é seguido pelo servidor quando o cliente chama a página de produtos/createProduct, por exemplo: <br>

* Cliente chama URL produtos/createProduct =>
* Servidor escuta chamada HTTP e redireciona para ./app/controllers/product.py =>
* Servidor verifica se existe a feature `createProduct` no controller e se esta feature permite receber o verbo HTTP desejado (exemplo, GET) => 
* Controller aciona a feature createProduct, processa a solicitação (fazendo interação com a camada de modelo se necessário) e retorna uma página HTTP ao usuário
