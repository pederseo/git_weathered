# import requests

# def obtener_clima_weatherstack(ciudad, api_key):
#     url = f"http://api.weatherstack.com/current?access_key={api_key}&query={ciudad}"

#     try:
#         # Realizamos la solicitud GET
#         respuesta = requests.get(url)

#         # Verificamos si la respuesta fue exitosa
#         respuesta.raise_for_status()  # Esto lanzará una excepción para códigos de error HTTP

#         # Convertimos la respuesta en formato JSON
#         datos = respuesta.json()

#         # Verificamos si la respuesta contiene un error relacionado con la API
#         if "error" in datos:
#             raise ValueError(f"Error en la API: {datos['error']['info']}")

#         # Extraemos la información relevante
#         temperatura = datos['current']['temperature']
#         descripcion = datos['current']['weather_descriptions'][0]
#         ciudad_nombre = datos['location']['name']
        
#         # Mostramos los datos obtenidos
#         print(f"El clima en {ciudad_nombre} es: {descripcion}")
#         print(f"La temperatura es de {temperatura}°C")

#     except requests.exceptions.RequestException as error_http:
#         print(f"Error en la solicitud HTTP: {error_http}")
#     except ValueError as error_api:
#         print(f"Error en la respuesta de la API: {error_api}")
#     except Exception as error_general:
#         print(f"Ocurrió un error inesperado: {error_general}")

# # Clave API de Weatherstack
# api_key = "98fd566897cb5779c402cc01a7840a98"

# # Ciudad de la que queremos obtener el clima
# ciudad = "paraguay"

# # Llamamos a la función
# obtener_clima_weatherstack(ciudad, api_key)


from api_key import APY_KEY
import requests

# Parámetros sin idioma
querystring = {"query": "paraguay"}

# solicitud a la API
response = requests.get(f"https://api.weatherstack.com/current?access_key={APY_KEY}", params=querystring)

# Obtener los datos JSON de la respuesta
data = response.json()

# Mostrar los datos si la solicitud fue exitosa
if "current" in data:
    ubicacion = data['location']['name']
    temperatura = data['current']['temperature']
    humedad = data['current']['humidity']

    print(f"Ubicación: {ubicacion}")
    print(f"Temperatura: {temperatura}°C")
    print(f"Humedad: {humedad}%")
else:
    print(f"Error: {data.get('error', 'No data available')}")
