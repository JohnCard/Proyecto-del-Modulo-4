# Cuando el usuario introduzca el nombre de un Pokémon, si no existe que le mande un mensaje de error; 
# si existe, que muestre una imagen y las estadísticas (peso, tamaño, movimientos, habilidades y tipos). 

# Posteriormente, guardarás toda la información del pokémon (junto con el link de la imagen frontal del 
# pokémon) en un archivo .json dentro de una carpeta llamada “pokedex”.

import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen

# Funciones a utilizar:   

# Función para obtener la info de un pokemon:
def get_pokemon_info(nombre_pokemon):
    '''
    Esta función va a hacer la petición http de acuerdo al nombre_pokemon que le pasamos como parametro, 
    formateandola en la cadena "url" que hemos creado, y en caso de que la petición get falle (400), llamamos 
    a la función validar_nombre()
    '''
    # utilizamos el lowercase() porque en la PokeApi, todos los nombres con los que se hace unua petición 
    # suelen ser en minusculas
    nombre_pokemon = input('Digite el nombre del pokemon a consultar: ').lower()
    url_peticion = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}')
    return url_peticion

answer = 's'
while(answer == ('s' or 'S')):
    nombre_pokemon = ''
    nombre_pokemon = get_pokemon_info(nombre_pokemon)
    
    # primero intentaremos obtener el json de la petición si la petición dio un "200", como tanto 
    # esperariamos 
    try:
        pokemon_jason = nombre_pokemon.json()
    except:
        print('La petición no funcionó! :( ')
    
    # despues, en vase a nuestros requirimientos, haremos un try, yaque en la api de 
    # "PokeAPI", al parecer no todos los pokemon cuentan con todos los atributos que otros si tienen,
    # por ejemplo, hay algunos que efectivamente cuantan con "img" propias que los pueden representar
    # graficamente como son o se ven en el anime, pero otros simplemente no la tienen, es por eso
    # que si en el siguiente try, uno de esos atributos no se llegase a encontrar, solo mandará un 
    # mensaje de advertencia, mas no fallará el programa :), y le preguntará al usuario si desea continuar.
    
    try:
        img = pokemon_jason["sprites"]["front_default"]
        imagen = Image.open(urlopen(img))
        plt.imshow(imagen)
        plt.title(f'''Nombre del pokemon: {pokemon_jason["name"].capitalize()}\nHabilidades: - {pokemon_jason["abilities"][1]["ability"]["name"]}\n           - {pokemon_jason["abilities"][0]["ability"]["name"]}''')
        plt.xlabel(f'''Peso: {pokemon_jason["weight"]}   Tamaño: {pokemon_jason["height"]}
Movimientos: {pokemon_jason["moves"][0]["move"]["name"]}''')
        plt.show()
    except:
        print(f'El pokemon {nombre_pokemon} no existe!')
            
    answer = input('Desea intentar con algún otro pokemon (S/N)? ')
    while(answer != 's' and answer != 'S' and answer != 'n' and answer != 'N'):
        answer = input(f'La respuesta {answer} es ¡INVÁLIDA!, intentelo de nuevo (S/N): ')
    if(answer == ('n' or 'N')):
        print('Gracias por confiar en nosotros, nos vemos la próxima, adios :).')
        exit()

lis = []
for i in range(30):
    lis.append((i+1))
print(lis)
u = 0; string = ''
# while(u<len(lis)):
    #  for i in range(5):
    #    i += 1
    #    string += str()
    
# experimento 2
for i in range(5,7):
    print(i)
