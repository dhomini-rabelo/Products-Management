<h1>Projeto com Django Rest Framework</h1>

<p>Projeto para gerenciar estoque de produtos de uma empresa</p>

<h2 style="margin-top: 30px;">🚀 Features</h2>

<li>Paginação</li>
<li>Autenticação</li>
<li>Cache</li>

<h2 style="margin-top: 30px;">🏷️ Modelagem do banco de dados</h2>

<h3>Produtos</h3>
<ul>
<li>ID</li>
<li>Nome</li>
<li>Preço</li>
<li>Quantidade</li>
<li>Categoria</li>
<li>Data de criação</li>
<li>Data de última modificação</li>
</ul>

<h3>Categoria</h3>
<ul>
<li>ID</li>
<li>Nome</li>
</ul>


<h2 style="margin-top: 30px;">🔗 APIs</h2>

<ul>


<li>
    <h3>/api/products</h3>
    <p>Lista de produtos com paginação</p>
    <img src="./readme/products/list_without_login.gif" alt="project-image" style="max-width: 100%; display: block; margin: 0 auto; margin-top: 20px;">
    <p style="margin-top: 20px;">Se usuário estiver autenticado ele poderá criar produtos com método POST</p>
    <img src="./readme/products/list_with_login.gif" alt="project-image" style="max-width: 100%; display: block; margin: 0 auto; margin-top: 20px;">
    <br>
</li>

<li>
    <h3>/api/products/[product-id]</h3>
    <p>Página para editar dados ou excluir um produto, no exemplo o ID do produto é 32</p>
    <img src="./readme/products/id_with_login.PNG" alt="project-image" style="max-width: 100%; display: block; margin: 0 auto; margin-top: 20px;">
    <p style="margin-top: 20px;">Para acessar esta página, o usuário deve estar autenticado, caso não esteja a requisição recebe um status code de 403 e a tela abaixo</p>
    <img src="./readme/products/id_without_login.PNG" alt="project-image" style="max-width: 100%; display: block; margin: 0 auto; margin-top: 20px;">
    <br>
</li>

<li>
    <h3>/api/products/filter</h3>
    <p>Lista todos os produtos apartir dos filtros indicados na url, neste caso é nome=mo e preço=10</p>
    <img src="./readme/products/filter.PNG" alt="project-image" style="max-width: 100%; display: block; margin: 0 auto; margin-top: 20px;">
    <p style="margin-top: 20px;">As KEYS indicam o nome do parâmetro que deve ser indicado na url, os VALUES indicam o tipo de filtro</p>
    <img src="./readme/products/filter_obj.PNG" alt="project-image" style="max-width: 100%; display: block; margin: 0 auto; margin-top: 20px;">
    <br>
</li>

<li>
    <h3>/api/categories</h3>
    <p>Lista de categorias com paginação</p>
    <img src="./readme/categories/list_without_login.PNG" alt="project-image" style="max-width: 100%; display: block; margin: 0 auto; margin-top: 20px;">
    <p style="margin-top: 20px;">Se usuário estiver autenticado ele poderá criar categorias com método POST, usando form html ou um JSON</p>
    <img src="./readme/categories/create.gif" alt="project-image" style="max-width: 100%; display: block; margin: 0 auto; margin-top: 20px;">
    <br>
</li>
    
<li>
    <h3>/api/products/[category-id]</h3>
    <p>Página para editar dados ou excluir um categoria, no exemplo o ID do produto é 2</p>
    <img src="./readme/categories/id_with_login.PNG" alt="project-image" style="max-width: 100%; display: block; margin: 0 auto; margin-top: 20px;">
    <p style="margin-top: 20px;">Para acessar esta página, o usuário deve estar autenticado, caso não esteja a requisição recebe um status code de 403 e a tela abaixo</p>
    <img src="./readme/categories/id_without_login.PNG" alt="project-image" style="max-width: 100%; display: block; margin: 0 auto; margin-top: 20px;">
    <br>
</li>

<li>
    <h3>/api/categories/filter</h3>
    <p>Lista todas as categorias apartir dos filtros indicados na url, neste caso é nome=i</p>
    <img src="./readme/categories/filter.PNG" alt="project-image" style="max-width: 100%; display: block; margin: 0 auto; margin-top: 20px;">
    <p style="margin-top: 20px;">Filtros</p>
    <img src="./readme/categories/filter_obj.PNG" alt="project-image" style="max-width: 100%; display: block; margin: 0 auto; margin-top: 20px;">
    <br>
</li>
    
</ul>
