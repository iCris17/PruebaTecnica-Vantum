# PruebaTecnica-Vantum

### Se usaron las siguientes tecnologías para el desarrollo de esta aplicación:
- Para el back-end: FastAPI
- Para el front-end: React

### Se usaron los IDE's:
- Para el back-end: PyCharm
- Para el front-end: Visual Studio Code

## ¿Cómo echar a andar el proyecto?
### Back-end:
#### Tomar en cuenta que estos pasos son totalmente efectivos en PyCharm 2024.3.4, aunque va a variar muy poco los pasos expuestos, según la versión del IDE
- En la esquina inferior derecha, se puede elegir el interpretador Python. Dar click en "Interpreter Settings..."
- Observamos que nos aparece un listado de los interpretadores (Python Interpreter) disponibles. Hacer click a la opción (al lado derecho del listado) que dice: "Add Interpreter"
- En Environment, ponemos "Generate New", y en Type, ponemos "Virtualenv". En Base python y Location no debería de modificarse nada. Se da OK.
- En la esquina inferior izquierda, hay un menú donde podemos abrir una terminal embebido en nuestro PyCharm (O bien Alt + F12). Una vez abierto, observaremos al lado izquierdo que dice (.venv), quiere decir que ya estamos usando el entorno virtual de nuestro proyecto.
- Ubicarse en la carpeta Backend/ListadoTareas
- Ejecutar los siguientes comandos:
-   **pip install fastapi 'uvicorn[standard]'**
-   **pip install pydantic**
- Una vez instaladas las dependencias, hacemos:
-   uvicorn listado.tareas.cmonroy.main:api

- ¡Felicidades! En este punto, habrás logrado levantar el API para generar un listado de tareas.
- Para ver que el API esté funcionando, entrar a la url: http://127.0.0.1:8000
- Para poder 'testear' la API, la url para su efecto es: http://127.0.0.1:8000/docs

**OJO: A veces la terminal embebida se queda colgada; para detener la API en Windows, entrar al navegador de tareas y buscar la aplicación en segundo plano llamada 'python.exe', luego dar 'Finalizar tarea'**

### Front-end:
#### Tomar en cuenta que estos pasos son totalmente efectivos en Visual Studio Code versión 1.109.5, aunque va a variar muy poco los pasos expuestos, según la versión del IDE
- En la pestaña 'Terminal', poner New (o nueva si el IDE está en español) terminal.
- Ubicarse en la carpeta Frontend/ListadoTareas
- Instalar primero las dependencias con **yarn install** y luego hacer un yarn dev.