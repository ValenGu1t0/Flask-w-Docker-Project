
### Trabajo Práctico Final para la materia Sistemas Operativos

El objetivo de este trabajo práctico es desarrollar y desplegar una aplicación web utilizando Docker y Docker Compose. La aplicación estará compuesta por dos servicios:

1. Una interfaz web en Python, servida por Apache HTTP Server.
2. Una base de datos MongoDB para almacenar información sobre juegos de mesa.


Requisitos que Faltan:

1. Docker Compose: Debe utilizarse Docker Compose para la orquestación de los
contenedores.

2. Contenedores:
- Contenedor de base de datos: Utilizar la imagen oficial de MongoDB.
- Contenedor de aplicación web: Crear una imagen personalizada a partir de un Dockerfile, basada en Apache HTTP Server con soporte para Python, PHP o Javascript.

5. Docker Compose: El archivo docker-compose.yml debe cumplir con los
siguientes requisitos:
- Redes y volúmenes: Configurar una red para que los contenedores puedan
comunicarse. Se recomienda utilizar volúmenes para persistir los datos de la
base de datos MongoDB.
- Variables de entorno: Definir variables de entorno necesarias para la
configuración de MongoDB (como el usuario, contraseña y nombre de la
base de datos).

6. Entrega: El ejercicio debe entregarse con:
- Un archivo docker-compose.yml que despliegue los dos servicios.
- Un Dockerfile para la creación de la imagen de la aplicación web con Apache.
- Código fuente de la aplicación web en Python.

7. Ejecución y pruebas:
- El proyecto debe ser ejecutable en cualquier entorno Docker, debe indicarse
como se hace el despliegue via algun archivo README.txt o similar.
- Debe mostrarse la aplicación funcionando con un ejemplo de alta, baja,
modificación y consulta de registros en la base de datos.