# BANCO DE OVA "GUIA"

This is GitHub's Ruby Style Guide, inspired by [RuboCop's guide][rubocop-guide].
recuarda que la guia esta junto al siguiente video de youtube: 

## Tabla de contenidos
1. [Publicacion nuevas OVA](#Publicacion-nuevas-OVA)
   1. [Container](#Container)
   2. [Partes del container](#Partes-del-container)
   3. [OVA Compuesto](#OVA-Compuesto)
   4. [Tipos de container en la pagina](#Tipos-de-container-en-la-pagina)
2. [Creacion de categorias](#Creacion-de-categorias)
   1. [Templates](#Templates)
   2. [App py](#App-py)
3. [Barra de navegacion](#Barra-de-navegacion)

## Publicacion nuevas OVA

### Container

* El container es una divicion espesifico en el que se guarda lo referente a una OVA

``` ruby
<div class = 'container p-4'>
    <div class="jumbotron" >
        <h1 class="display-4">Titulo</h1>
        <p class="lead">Informacion sobre la OVA</p>
        <hr class="my-4">
        <iframe src="Link OVA" width="640" height="480"></iframe>
        <a class="btn btn-danger btn-lg" href="Link OVA" target="_blank" role="button">Ver completo</a>
    </div>
</div>
```

* Tiene una estetica espesifica dentro del pagina dada por la clase `jumbotron`

``` ruby
.jumbotron {
    margin-top: 2rem;
    padding: 4rem 2rem;
    margin-bottom: 2rem;
    border-radius: .3rem;  
    background-color: #212529;
    color: #fff;
  }
```
<img src="https://cdn.discordapp.com/attachments/827534398064295948/1023277440111497216/unknown.png">


### Partes del container


* `h1` corresponde a el texto que se va a ver mas grande dentro de la pagina por lo que se utiliza para los titulos.

``` ruby
<h1 class="display-4">Texto a mostrar</h1>
```
<img src="https://cdn.discordapp.com/attachments/827534398064295948/1023280023668527155/unknown.png">


* `p` corresponde a el texto que es utilizado para mostrar informacion importante de la ova antes de mostrar el documento,
tambien se utiliza al final del container para mostrar autores y referencias.

``` ruby
<p class="lead">Informacion sobre la OVA</p>
```
<img src="https://media.discordapp.net/attachments/827534398064295948/1023281298116194344/unknown.png">


* `hr` corresponde a una linea que separa el contenido

``` ruby
<hr class="my-4">
```
<img src="https://cdn.discordapp.com/attachments/827534398064295948/1023282744811335771/unknown.png">


* `iframe` corresponde a la OVA espesifica, dentro de `src` se coloca el link para poder visualizarla independientemente del formato

``` ruby
<iframe src="Link OVA" width="640" height="480"></iframe>
```
<img src="https://cdn.discordapp.com/attachments/827534398064295948/1023284203552522301/unknown.png">


* `a` corresponde a un boton, dentro de `href` se coloca el link del vinculo, este no es absolutamente necesario

``` ruby
<a class="btn btn-danger btn-lg" href="Link OVA" target="_blank" role="button">Ver completo</a>
```
<img src="https://cdn.discordapp.com/attachments/827534398064295948/1023284995307085914/unknown.png">

### OVA Compuesto

* El ejemplo anterior solo representa un OVA unico, es decir, que solo cuenta con un archivo que lo compone; en el caso de tener un OVA multiple, es decir,
que cuenta con multiples achivos que lo componen, se implementa de la siguiente manera

``` ruby
<div class = 'container p-4'>
    <div class="jumbotron" >
        <h1 class="display-4">Titulo principal</h1>
        <p class="lead">Caracteristicas de la OVA</p>
        <hr class="my-4">
        <p class="lead">Nombre o formato del primer archivo</p>
        <iframe src="Link primer archivo" width="640" height="480"></iframe>
        <p class="lead">Nombre o formato del segundo archivo</p>
        <iframe src="Link segundo archivo" width="640" height="480"></iframe>
        <p class="lead">Nombre o formato del tercer archivo</p>
        <iframe src="Link tercer archivo" width="640" height="480"></iframe>
        <p class="lead">Nombre o formato del cuarto archivo</p>
        <iframe src="Link cuarto archivo" width="640" height="480"></iframe>
        <hr class="my-4">
        <p class="lead">Autor de la OVA</p>
    </div>
</div>
```
<img src="https://user-images.githubusercontent.com/114035558/192112404-9854d78a-3233-4441-a731-6dd1af6c387d.png">

* Se pueden colocar cuantos archivos contenga la OVA independientemente del formato o la cantidad, cada archivo se compone de dos partes que se editan por archivo

``` ruby
<p class="lead">Nombre o formato del archivo</p>
<iframe src="Link del archivo" width="640" height="480"></iframe>
```

### Tipos de container en la pagina

los containers con los que trabajamos anteriormente eran containers para OVA, pero no son los unicos que se utilizan dentro de la pagina, esto depende el la aplicacion que se le de, y cada uno tiene su propia configuracion, organizacion y conjunto de partes

*Container de Subcategorias

Este container se utiliza para que, por ejemplo, dentro de los cursos se encuentren las asignaturas y puedan acceder a las OVA de esa asignatura y grado espesifico

```ruby
<div class="jumbotron">
        <h1 class="display-4">Nombre de la asignatura o subcategoria</h1>
        <p class="lead">Descripcion de la asignatura o subcategoria</p>
        <hr class="my-4">
        <p>haz click aqui para ver todas actividades relacionadas con esta materia</p>
        <a class="btn btn-danger btn-lg" href="ruta de la template a mostrar como aparece en App.py" role="button">Click aqui</a>
</div>

```

* Container de Apps y paginas recomendadas

Este container se utiliza dentro de la categoria de Apps y paginas recomendadas, y contienen informacion y el hipervinculo de una aplicacion o pagina que los estudiantes pueden usar dentro de su proceso educativo

```ruby
<div class="jumbotron" >
        <h1 class="display-4">Nombre de la aplicacion o pagina</h1>
        <p class="lead">descripcion corta de la aplicacion o pagina</p>
        <hr class="my-4">
        <p>Descripcion de la aplicacion o pagina</p>
        <a class="btn btn-danger btn-lg" href="Link de la aplicacion o pagina" 
        target="_blank" role="button">Click aqui</a>
    </div>
```

* Container de Bienvenida

Estos se utilizan en la mayoria de categorias, y contienen caracteristicas de la categoria

```ruby
    <div class="jumbotron" >
        <h1 class="display-4">Bienvenido</h1>
        <p class="lead">Descripcion de lo que se localiza dentro de la categoria</p>
    </div>
```

## Creacion de categorias

Para la creacion de categorias nuevas se necesita agregar una nueva Template y agregar la ruta a `App.py`

### Templates

* Dentro de `template/` genera un nuevo archivo, si la categoria que se quiere agregar hace parte de una categoria mas grande, como por ejemplo un grado, entonces agregaras el grado primero despues la asignatura a la que hace parte y un `.html`, por ejemplo `6musica.html`; dentro de este archivo coloca el siguiente codigo

``` ruby
{% extends "layout.html" %}

{% block content %}

{% endblock %}
```

la template ya esta lista para que empieces a agregar OVA, recuarda que tienes que agregarlo entre `{% block content %}` y `{% endblock %}`

### App py

*Ahora para que puedas utilizar la template dentro de la pagina, tienes que primero agregarla a `App.py` para esto primero entra este archivo .py, ahora genera una ruta con el siguiente formato

```ruby
@app.route('')
def #():
    return render_template('Nombre.html')
```
* Para el siguiente ejemplo supondremos que queremos agregar musica a sexto o agregar la categoria de PRAE en la pagina

* Entre las `''` de `@app.route('')` coloca / + el nombre con el que va a aparecer y vas a llamar a la template dentro de la pagina, en caso de que sea una subcategoria, coloca primero /nombre de la categoria grande/nombre de la nueva template, recuarda que lo que coloques sera la ruta que usaras para llamar la template desde cualquier otra template dentro de la pagina

```ruby
@app.route('/6/Musica')
```

```ruby
@app.route('/PRAE')
```

* Remplaza el `#` de `def #():` y en el coloca un nombre alusivo a el grado y asignatura, o la categoria en minuscula
```ruby
def sixmusica():
```
```ruby
def prae():
```

* ahora en `return render_template('Nombre.html')`, entre los `()` coloca el nombre de la template que quieres mostrar
```ruby
return render_template('6musica.html')
```
```ruby
return render_template('PRAE.html')
```
El resultado seria el siguiente, recuarda que estas rutas en caso de ser parte de una categoria mas grande van en debajo de la ruta de la categoria de la que hacen parte, si son independientes, van debajo de la ruta `'/first_page'`

```ruby
@app.route('/6/Musica')
def sixmusica():
    return render_template('6musica.html')
```
```ruby
@app.route('/PRAE')
def prae():
    return render_template('PRAE.html')
```

## Barra de navegacion

<img src="(https://media.discordapp.net/attachments/827534398064295948/1023300555398987829/unknown.png">

* Se pueden agregar hipervinculos a la barra superior para generar o agilizar la entrada a una categoria, la barra de navegacion se encuentra dentro de
`template/layout.html`

``` ruby
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="/first_page">Apuntes GNF</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-   expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="/first_page">Home</a>
                        </li>
                        <li class="nav-item">
                                <a class="nav-link" href="/6">6°</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/7">7°</a>
                        </li>
                        <li class="nav-item">
                                <a class="nav-link" href="/8">8°</a>
                        </li>
                        <li class="nav-item">
                                <a class="nav-link" href="/9">9°</a>
                        </li>
                        <li class="nav-item">
                                <a class="nav-link" href="/10">10°</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/11">11°</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/Prae">PRAE</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/recomendados">Aplicaciones y Paginas</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/about">About</a>
                        </li>
                    </ul>
                </div>
        </div>
    </nav>
```
* Cada vinculo de la barra se encuentra contenido en un `li`

``` ruby
</li>
<li class="nav-item">
<a class="nav-link" href="/Nombre">Texto a mostrar</a>
</li>
```
* Para editarlo en `href` se coloca el link del vinculo que se quiere mostrar, si es una template la que se quiere mostrar se coloca el `/nombre` que se le coloco en `App.py`; y entre los `>` y `<` se coloca el nombre como va a aparecer el vinculo dentro de la barra

