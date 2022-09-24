# BANCO DE OVA "GUIA"

This is GitHub's Ruby Style Guide, inspired by [RuboCop's guide][rubocop-guide].
recuarda que la guia esta junto al siguiente video de youtube: 

## Tabla de contenidos
1. [Publicacion nuevas OVA](#Publicacion-nuevas-OVA)
   1. [Container](#Container)
   2. [Partes del container](#Partes-del-container)
   3. [OVA Compuesto](#OVA-Compuesto)
2. [Creacion de categorias](#Creacion-de-categorias)
   1. [Templates](#Templates)
   2. [App.py](#App.py)
   3. [Inplementacion](#Inplementacion)
3. [Barra de navegacion](#Barra-de-navegacion)
4. [Formatos](#Formatos)

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
<img src="https://cdn.discordapp.com/attachments/827534398064295948/1023277440111497216/unknown.png" height="585">


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

## Creacion de categorias

### Templates

### App.py

### Inplementacion

## Barra de navegacion

## Formatos
