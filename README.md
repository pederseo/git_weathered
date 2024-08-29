# git_weathered

## Descripción
**git_weathered** es una aplicación de línea de comandos (CLI) que integra el uso de Git y GitHub para manejar conexiones, ramas, hooks, releases, pruebas y etiquetas. Además, permite obtener datos del clima a través de una API. Esta herramienta está diseñada para facilitar el manejo de proyectos en GitHub mientras se accede a información meteorológica relevante.

## Tecnologías utilizadas
- **Python**
- **Git**
- **GitHub**
- **API del clima**
- **argparse**

## Requisitos previos
Antes de utilizar **git_weathered**, asegúrate de tener instaladas las siguientes bibliotecas:

- `requests`
- `black`
- `flake8`

## Instrucciones de instalación

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/pederseo/git_weathered.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd git_weathered
   ```

3. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```

4. Activa el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```

## Instrucciones de uso

Para comenzar a utilizar **git_weathered**, ejecuta el siguiente comando en tu terminal:

```bash
python main.py --help
```

Esto mostrará una lista de comandos disponibles y opciones para interactuar con la aplicación.

## Autor
- Olaf Pedersen Torales

---

Este README cubre todos los aspectos clave que mencionaste. Puedes personalizarlo aún más si lo deseas.
# instrucciones de instalacion
- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt
- run clima.py