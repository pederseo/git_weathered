# Interfaz CLI (GitBash nano)
- aplicacion CLI
- pedir alusuario que ingrese su ubicacion (pais,ciudad)
- consulta a la API (temperatura, condiciones, etc)

# Git
- hacer un commit inicial para la base del proyecto
- crear rama para trabajar en la obtencion de datos
- hacer commints por cada cambio importante
- Implementa un hook de pre-commit que verifique la calidad del código antes de que se permita realizar un commit. 

# estructura de archivos
ejercicio_9
    |_main.py
    |_conexion_api.py
        |_.git/hooks/pre-commit.

# comandos
--help

- filtrar por ubicacion
- exportar (JSON, CSV, Texto plano)
- incluir mensaje de ayuda --help que explique como usar la aplicacion y los comandos

___
Una vez completada la funcionalidad básica, crea una etiqueta anotada (ejemplo: git tag -a v1.0
-m "Versión 1.0 - Funcionalidad básica completada") y empújala al repositorio remoto. Luego,
crea un release en GitHub, documentando lo que incluye esta versión.
___

# Scrips
- chmod +x .git/hooks/pre-commit
- pip install -r requirements.txt
- python main.py --location "asuncion paraguay" --format "json"
- pytest test/

# funciones 
- funcion caching para almacenar los resultados de consultas repetitivas a la API y reducir el número de solicitudes realizadas.
- funcion consultar el clima de varias ubicaciones en una sola ejecución del
comando, mostrando un resumen o un informe detallado de cada ubicación.
- mensaje de errores: 
    Informa si los datos no están disponibles para la ubicación solicitada 
    ofrece soluciones
    como verificar la ortografía de la ubicación

___

# instrucciones

## activar entorno virtual

- python -m venv venv

- venv\Scripts\activate

- pip install requirements

- run clima.py