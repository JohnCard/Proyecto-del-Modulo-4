import requests

# Datos de openweather API para obtener el clima de distintas localidades:
# por el id de la ciudad: https://api.openweathermap.org/data/2.5/weather?id={city id}&appid={API key}

# por la lon y lat de la ciudad: https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

# por el nombre de la ciudad: https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

# por el codigo (el postal y el de la ciudad): https://api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={API key}

# Funciones a utilizar:

# Función para validar coordenadas
def validar_dato(coordenada,tipo_coordenada):
    while True:
        try:
            coordenada = (input(f'Digite su {tipo_coordenada}: '))
            # esto lo hacemos para asegurarnos de que lo que digitó fue un numero
            float(coordenada)
            break
        except ValueError:
            print(f'La {tipo_coordenada} ¡ES INVÁLIDA!, intentelo de nuevo!.')
    return str(coordenada)

# Función para validar numeros enteros
def validar_entero(dato_entero,tipo_dato):
    dato_entero = input(f'Digite su {tipo_dato} por favor: ')
    while(dato_entero.isnumeric() == False):
        dato_entero = input(f'El dato {tipo_dato} digitado es ¡INCORECTO!, favor de digitar su {tipo_dato} de nuevo: ')
    return dato_entero

# sin embargo, realizaremos un programa aún mas dinamico, solicitando todo
# lo necesario para pronosticar el tiempo o las condiciones en que se en-
# cuentra un determinado lugar bajo ciertas condiciones, como son las 
# coordenadas que el usuario digite, asi:

answer = 's'
while(answer == ('s' or 'S')):
    api_key = input('Digite su Api_Key: ')
    while(api_key.isidentifier() == False):
        api_key = input(f'La Api Key {api_key} digitada ¡NO ES VÁLIDA!, favor de digitarla de nuevo: ')
    print('''Usted puede consultar su longitud y la altitud de su ciudad en el siguiente link: 
https://www.coordenadas-gps.com/
Usted decide con cuales parametros buscar una ciudad:
1) por el id de la ciudad
2) por la longitud y latitud de la ciudad
3) por el nombre de la ciudad
4) por el codigo (el postal y el de la ciudad)
''')
    indice = input('Digite el indice con el que desea trabajar (1/2/3/4): ')
    while(indice != '1' and indice != '2' and indice != '3' and indice != '4'):
        indice = input(f'Su respuesta {indice} es ¡INVÁLIDA!, favor de intentarlo de nuevo (1/2/3/4): ')
    if(indice == '1'):
        id_city = ''
        id_city = validar_entero(id_city,'id')
        peticion = requests.get(f'https://api.openweathermap.org/data/2.5/weather?id={id_city}&appid={api_key}')
    elif(indice == '2'):
        longitud = ''
        longitud = validar_dato(longitud,'longitud')
        latitud = ''
        latitud = validar_dato(latitud,'latitud')
        peticion = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={api_key}')
    elif(indice == '3'):
        city_name = input('Digite el nombre de su ciudad: ').title()
        peticion = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}')
    elif(indice == '4'):
        codigo_postal = ''
        codigo_postal = validar_entero(codigo_postal,'codigo postal')
        country_code = input('Digite el codigo de su pais: ').upper()
        peticion = requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={codigo_postal},{country_code}&appid={api_key}')

    try: 
        json_file = peticion.json()
        print(f'Condiciones de la ciudad {json_file["name"]}: {json_file["weather"][0]["main"]} ')
    except:
        print(f'Los datos introducidos resultarón ivalidos. ')
    answer = input('Desea reintentar con datos distintos para otra ciudad (S/N): ')
    while(answer != 'n' and answer != 'N' and answer != 's' and answer != 'S'):
        answer = input(f'Su respuesta {answer} es ¡INVÁLIDA!, favor de intentarlo de nuevo (S/N): ')

    if(answer == ('n' or 'N')):
        exit()
