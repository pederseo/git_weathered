# import csv
# import requests


# class Clima:
#     def __init__(self, pais, formato):
#         self.pais = pais
#         self.formato = formato
#         self.data = self.solicitud_api()

#     def solicitud_api(self):
#         '''Realiza la solicitud a la API del clima y retorna los datos en formato JSON.'''
#         response = requests.get(f"https://api.weatherstack.com/current?access_key={APY_KEY}", params={"query": self.pais})
#         return response.json()

#     def formato_json(self):
#         '''Devuelve los datos del clima en formato JSON.'''
#         try:
#             if "current" in self.data:
#                 ubicacion = self.data['location']['name']
#                 temperatura = self.data['current']['temperature']
#                 humedad = self.data['current']['humidity']

#                 resultado = {
#                     'ubicacion': ubicacion,
#                     'temperatura': temperatura,
#                     'humedad': humedad
#                 }
#                 return resultado
#             else:
#                 return f"Error en la respuesta de la API: {self.data.get('error')}"
            
#         except requests.exceptions.RequestException as e:
#             return f"Error en la solicitud: {e}"

#     def formato_csv(self):
#         '''Guarda los datos del clima en un archivo CSV.'''
#         try:
#             if "current" in self.data:
#                 ubicacion = self.data['location']['name']
#                 temperatura = self.data['current']['temperature']
#                 humedad = self.data['current']['humidity']

#                 resultado = {
#                     'ubicacion': ubicacion,
#                     'temperatura': temperatura,
#                     'humedad': humedad
#                 }

#                 with open(f'{self.pais}_clima.csv', mode='w', newline='') as file:
#                     writer = csv.DictWriter(file, fieldnames=resultado.keys())
#                     writer.writeheader()
#                     writer.writerow(resultado)

#                 return f"Datos guardados en {self.pais}_clima.csv"
#             else:
#                 return f"Error en la respuesta de la API: {self.data.get('error')}"
            
#         except requests.exceptions.RequestException as e:
#             return f"Error en la solicitud: {e}"

#     def formato_texto(self):
#         '''Devuelve los datos del clima en formato de texto plano.'''
#         try:
#             if "current" in self.data:
#                 ubicacion = self.data['location']['name']
#                 temperatura = self.data['current']['temperature']
#                 humedad = self.data['current']['humidity']

#                 resultado = (f"Ubicación: {ubicacion}\n"
#                              f"Temperatura: {temperatura}°C\n"
#                              f"Humedad: {humedad}%")
                
#                 return resultado
#             else:
#                 return f"Error en la respuesta de la API: {self.data.get('error')}"
            
#         except requests.exceptions.RequestException as e:
#             return f"Error en la solicitud: {e}"

#     def obtener_clima(self):
#         '''Devuelve los datos del clima en el formato solicitado por el usuario.'''
#         if self.formato == 'json':
#             return self.formato_json()
#         elif self.formato == 'csv':
#             return self.formato_csv()
#         elif self.formato == 'texto':
#             return self.formato_texto()
#         else:
#             return "Formato no reconocido. Por favor, elija 'json', 'csv' o 'texto'."

# # Ejemplo de uso
# clima = Clima('Paraguay', 'json')
# print(clima.obtener_clima())

# clima_csv = Clima('Paraguay', 'csv')
# print(clima_csv.obtener_clima())

# clima_texto = Clima('Paraguay', 'texto')
# print(clima_texto.obtener_clima())

import requests
from api_key import APY_KEY
import json

def get_weather(pais):
    '''oftener datos de la api'''
    url = f"https://api.weatherstack.com/current?access_key={APY_KEY}"
    
    response = requests.get(url, params={"query": pais})
    if response.status_code == 200:
        data = response.json()
        return data
    
    else:
        return f"Error en la respuesta de la API: {data.get('error')}"


def format_as_text(weather_data):
    return f"City: {weather_data['name']}\nTemperature: {weather_data['main']['temp']}°C\nWeather: {weather_data['weather'][0]['description']}"

def format_as_json(weather_data):
    return json.dumps(weather_data, indent=4)

def format_as_csv(weather_data):
    return f"city,temperature,weather\n{weather_data['name']},{weather_data['main']['temp']},{weather_data['weather'][0]['description']}"