#### PruebaTecnica-Vantum

### Se usaron las siguientes tecnologías para el desarrollo de esta aplicación:
- Para el back-end: FastAPI

### Se usaron los IDE's:
- Para el back-end: PyCharm

### ¿Cómo echar a andar el proyecto?
## Back-end:
# Tomar en cuenta que estos pasos son totalmente efectivos en PyCharm 2024.3.4
- En la esquina inferior derecha, se puede elegir el interpretador Python. Dar click en "Interpreter Settings..."
- Observamos que nos aparece un listado de los interpretadores (Python Interpreter) disponibles. Hacer click a la opción (al lado derecho del listado) que dice: "Add Interpreter"
- En Environment, ponemos "Generate New", y en Type, ponemos "Virtualenv". En Base python y Location no debería de modificarse nada. Se da OK.
- En la esquina inferior izquierda, hay un menú donde podemos abrir una terminal embebido en nuestro PyCharm (O bien Alt + F12). Una vez abierto, observaremos al lado izquierdo que dice (.venv), quiere decir que ya estamos usando el entorno virtual de nuestro proyecto.
- Ejecutar los siguientes comandos:
-   pip install fastapi 'uvicorn[standard]'
-   pip install pydantic
- Una vez instaladas las dependencias, hacemos:
-   uvicorn listado.tareas.cmonroy.main:api

- ¡Felicidades! En este punto, habrás logrado levantar el API para generar un listado de tareas.
- Para ver que el API esté funcionando, entrar a la url: http://127.0.0.1:8000
- Para poder 'testear' la API, la url para su efecto es: http://127.0.0.1:8000/docs

**OJO: A veces la terminal embebida se queda colgada; para detener la API en Windows, entrar al navegador de tareas y buscar la aplicación en segundo plano python.exe, luego dar 'Finalizar tarea'**