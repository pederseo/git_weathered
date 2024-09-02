import argparse
from funciones import *

def parse_arguments():
    parser = argparse.ArgumentParser(description='obtener informacion del clima de un pais.')

    parser.add_argument(
        '--pais', 
        type=str, 
        help='nombre del pais')
    
    parser.add_argument(
        '--ciudad', 
        type=str, 
        help='nombre de la ciudad')
    
    parser.add_argument(
        '--formato', 
        choices=['texto', 'json', 'csv'], 
        type=str, 
        help='formato de salida (text, json, csv)')
    
    return parser.parse_args()


args = parse_arguments()

try:
    weather_data = get_weather(args.pais, args.ciudad)

except:
    print("error al traer informacion de la api")
    
if args.formato == 'texto':
    output = formato_texto(weather_data ,args.pais, args.ciudad)

elif args.formato == 'json':
    output = formato_json(weather_data ,args.pais, args.ciudad)

elif args.formato == 'csv':
    output = formato_csv(weather_data ,args.pais, args.ciudad)

else:
    print('ingresa un formato valido (json, texto, csv)')
    
print(output)
