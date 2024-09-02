import requests
from api_key import APY_KEY


def get_weather(pais, ciudad):
    """Obtener datos de la API del clima utilizando el país y la ciudad"""
    query = f"{ciudad},{pais}"
    url = f"https://api.weatherstack.com/current?access_key={APY_KEY}"

    response = requests.get(url, params={"query": query})

    if response.status_code == 200:
        data = response.json()
        return data

    else:
        return f"Error en la respuesta de la API: {data.get('error')}"


# ___________________________________________________________________________________________


def formato_texto(weather_data, pais, ciudad):
    """mostrar datos en formato de texto"""
    current = weather_data["current"]
    format_text = f"""
pais: {pais}
ciudad: {ciudad}
Temperatura: {current.get('temperature')} C
Humedad: {current.get('humidity')} %"""
    return format_text


# ____________________________________________________________________________________________


def formato_json(weather_data, pais, ciudad):
    """mostrar datos en formato json"""
    if "current" in weather_data:
        current = weather_data["current"]

        # Crear un diccionario con solo la temperatura y la humedad
        format_json = {
            "pais": pais,
            "ciudad": ciudad,
            "Temperatura": f"{current.get('temperature')} C",
            "Humedad": f"{current.get('humidity')} %",
        }
    return format_json


# _____________________________________________________________________________________________


def formato_csv(weather_data, pais, ciudad):
    """mostrar datos en formato csv"""
    current = weather_data["current"]

    # Crear las cabeceras
    headers = "Pais,Ciudad,Temperatura (C),Humedad (%)"

    # Crear la fila de datos
    data_row = f"{pais},{ciudad},{current.get('temperature')},{current.get('humidity')}"

    # Combinar cabeceras y datos en formato CSV
    csv_output = f"{headers}\n{data_row}"

    return csv_output
