import argparse
from funciones import *

def parse_arguments():
    parser = argparse.ArgumentParser(description='obtener informacion del clima de un pais.')
    parser.add_argument(
        '--pais', 
        type=str, 
        help='nombre del pais')
    parser.add_argument(
        '--format', 
        choices=['text', 'json', 'csv'], 
        default='text', 
        help='formato de salida (text, json, csv)')
    
    return parser.parse_args()

def main():
    args = parse_arguments()

    try:
        weather_data = get_weather(args.pais)

    except ValueError as e:
        print(e)
    
    if args.format == 'text':
        output = format_as_text(weather_data)
    elif args.format == 'json':
        output = format_as_json(weather_data)
    elif args.format == 'csv':
        output = format_as_csv(weather_data)
    
    print(output)

if __name__ == "__main__":
    main()
