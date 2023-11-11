# Taller IA con RAGs 

En este taller creamos una portal donde podremos hacer preguntas sobre diferentes carreras de la escuela colombiana de ingenieria, para ello usamos una base de datos Pinecone
donde guardamos toda la informacion sobre estas carrearas, luego en base a un query del usuario, usamos una IA para leer estos archivos y obtener una respuesta 

## Iniciando

Estas instrucciones te ayudarán a tener una copia de este proyecto corriendo en tu máquina local, en donde podras hacer pruebas o desarrollar sobre él 

### Prerrequisitos

* Git 
* Python
* Pip

Si aún no tienes instaladas estas tecnologias, los siguientes tutoriales te pueden ayudar

* Git: https://www.youtube.com/watch?v=4xqVv2lTo40
* Python: https://www.python.org/downloads/
* Pip: https://pip.pypa.io/en/stable/installation/

### Instalando el proyecto

Para hacer una copia local del proyecto, debes abrir tu terminal, dirigirte al directorio donde quieras que este el proyecto y usar el siguiente comando

```
git clone https://github.com/DanielOchoa1214/Lab7-AREP.git
```

Luego muevete al directorio creado y desde ahi ejecuta los siguientes comandos

```
pip install langchain
pip install openai==0.27.8
pip install flask
pip install pinecone-client
pip install tiktoken
pip install requests
```

Y para iniciar el servidor solo deber correr el archivo eci_controller.py

Ya que la aplicación haya iniciado, puedes dirigirte a tu navegador de preferencia y entrar en https://localhost:5000 para ver la app corriendo, en ella encontraras una muy bonita página que cree con mucho esfuerzo donde puedes hacer tus preguntas

<img width="433" alt="Screenshot 2023-11-11 at 1 14 32 PM" src="https://github.com/DanielOchoa1214/Taller-IA/assets/77862016/6f45f465-4d72-4959-844b-88e18d1cc88b">

Para preguntar solo ingresa la pregunta y dale click en el boton de enviar, si todo sale bien deberia aparecerte mas abajo la respouesta a tu pregunta

<img width="838" alt="Screenshot 2023-11-11 at 1 16 41 PM" src="https://github.com/DanielOchoa1214/Taller-IA/assets/77862016/b8018e64-2551-43fe-bb74-cd89dc19957e">

## Construido con

* Amor
* [Python](https://www.python.org/) - Lenguaje de programación
* [PyCharm IDEA](https://www.jetbrains.com/es-es/pycharm/) - IDE de desarrollo

## Version

1.0-SNAPSHOT

## Autores

Daniel Sebastián Ochoa Urrego - [DanielOchoa1214](https://github.com/DanielOchoa1214)

## Licencia

GNU General Public License family
## Agradecimientos

* A nuestro querido profesor de Arquitectura empresariales Daniel Benavides
* Jorge, el mejor monitor 
* Figo, mi hermoso perro


