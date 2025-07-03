
### Trabajo Práctico Final para la materia Sistemas Operativos

El objetivo de este trabajo práctico fue desarrollar y desplegar una aplicación web utilizando Docker y Docker Compose. La aplicación se compone por dos servicios:

1. Una interfaz web en Python, servida por Apache HTTP Server.

2. Una base de datos MongoDB para almacenar información sobre juegos de mesa.

La aplicación web fue desarrollada con Flask de Python, HTML y Tailwind CSS para estilar. La misma funciona como un CRUD de juegos de mesa. Los datos se persisten en una base de datos no relacional MongoDB. 

Se creó una imagen personalizada a partir de esta app web basada en Apache HTTP Server con Dockerfile, y se usó la imagen oficial de MongoDB para la base. Ambos servicios fueron comunicados y orquestados gracias a Docker Compose. Además, estos se comunican a través de la red appnet y se utilizó un volumen en la imagen de Mongo para persistir los datos en mi maquina local. Las variables de entorno fueron definidas acordes a la app web y mongo y están configuradas para poder usar la app base. El volumen físico de la data persistida se llama mongodb_data.

Además, se agregó el archivo 000-default.yml, el cual es la configuración por defecto de Apache para servir un sitio web. Apache tiene archivos de configuración llamados virtual hosts, que permiten definir cómo se va a servir un sitio. El 000-default.conf es uno de esos archivos y viene por defecto. Fue editado para decirle a Apache que use mod_wsgi y ejecute mi aplicación Flask a través del archivo wsgi.py.

## Ejecución y pruebas:

La aplicacion actual esta diseñada para probar Docker y Docker Compose, por lo que su lógica no es muy compleja. Podes clonar el repositorio de la app desde: https://github.com/ValenGu1t0/Flask-w-Docker-Project.git, y una vez lo tengas en tu máquina, abrirlo.

!! ATENCION !! Se requiere tener Docker Desktop o Engine en la computadora para poder levantar y ejecutar los contenedores; antes de abrir la app, se deben inicializar para pdoer reconocer los comandos de Docker. 

Una vez se clonó el repo, y se abrió Docker Desktop, es tan fácil como posicionarse en la raíz del proyecto y ejecutar:

`docker-compose up --build`

Esto inicializará los contenedores, y para poder ver la app funcionando, se debe acceder [localhost:8080](http://localhost:8080) para ver la app funcionando.

Cuando terminemos de testear o probar la app, ingresamos: 

`docker-compose down` 

Y esto eliminará los contenedores (y la data si no fue persistida), liberando recursos de tu maquina y pausando la ejecución de los mismos. 