# Funciones a utilizar:

# Función para pedir el nombre de un pokemon que si exista:
def validar_nombre(nombre_pokemon):
    '''
    Esta función recibe como parametro el nombre_pokemon, lo procesa en la condición del ciclo while, y si
    la petición en la pokeapi lanza el error ":undefined", el ciclo no dejará de solicitar un nombre
    hasta que sea correcto.
    '''

# Función para obtener la info de un pokemon:
def get_pokemon_info(nombre_pokemon):
    '''
    Esta función va a hacer la petición http de acuerdo al nombre_pokemon que le pasamos como parametro, formateandola
    en la cadena "url" que hemos creado, y en caso de que la petición get falle (400), llamamos a la función 
    validar_nombre()
    '''
    nombre_pokemon = input('Digite el nombre del pokemon a consultar: ').lowercase()
    url = f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}'
    url_peticion = request.get(url)

import request
import matplotlib



answer = 's'
while(answer == ('s' or 'S')):

