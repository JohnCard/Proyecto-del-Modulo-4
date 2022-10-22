import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen
import json

def graficar(posicion,mensaje,texto,font_size):
    plt.subplot(3,3,posicion)
    plt.axis([0,20,5,0])
    plt.title(mensaje)
    plt.text(1,4, texto,fontsize=font_size)

def retornar_texto(atributo,atributo_dos):
    cont = 0
    texto = ''
    lista_atributo = []
    if(cont+5 > len(pokemon_jason[f"{atributo}"])):
        cont = -1
        for i in pokemon_jason[f"{atributo}"]:
            cont += 1
            texto += pokemon_jason[f"{atributo}"][cont][f"{atributo_dos}"]["name"]+', '
            lista_atributo.append(pokemon_jason[f"{atributo}"][cont][f"{atributo_dos}"]["name"])
    else:
        cont = 0
        texto = ''        
        while(cont < len(pokemon_jason[f"{atributo}"])):
            if(cont+5 > len(pokemon_jason[f"{atributo}"])):
                for i in range(cont,len(pokemon_jason[f"{atributo}"])):
                    texto += pokemon_jason[f"{atributo}"][i][f"{atributo_dos}"]["name"]+', '
                    lista_atributo.append(pokemon_jason[f"{atributo}"][cont][f"{atributo_dos}"]["name"])
            else:
                for i in range(cont,cont+5):
                    texto += pokemon_jason[f"{atributo}"][i][f"{atributo_dos}"]["name"]+', '
                    lista_atributo.append(pokemon_jason[f"{atributo}"][cont][f"{atributo_dos}"]["name"])
                texto += '\n'
            cont += 5
    return texto + 'etc.',lista_atributo

file = open('archivo_uno.json','r')
lista_archivo = json.loads(file.read())
file.close()

# Cuando el usuario introduzca el nombre de un Pokémon, si no existe que le mande un mensaje de error; 
# si existe, que muestre una imagen y las estadísticas (peso, tamaño, movimientos, habilidades y tipos). 

# Posteriormente, guardarás toda la información del pokémon (junto con el link de la imagen frontal del 
# pokémon) en un archivo .json dentro de una carpeta llamada “pokedex”.

answer = 's'
lista_diccionarios = []
while(answer == ('s' or 'S')):
    nombre_pokemon = input('Digite el nombre del pokemon a consultar: ').lower()
    url_peticion = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}')
    
    # primero intentaremos obtener el json de la petición si la petición dio un "200", como tanto 
    # esperariamos 
    try:
        pokemon_jason = url_peticion.json()
    except:
        print('La petición no funcionó! :( ')
    
    # despues, en vase a nuestros requirimientos, haremos un try, yaque en la api de 
    # "PokeAPI", al parecer no todos los pokemon cuentan con todos los atributos que otros si tienen,
    # por ejemplo, hay algunos que efectivamente cuantan con "img" propias que los pueden representar
    # graficamente como son o se ven en el anime, pero otros simplemente no la tienen, es por eso
    # que si en el siguiente try, uno de esos atributos no se llegase a encontrar, solo mandará un 
    # mensaje de advertencia, mas no fallará el programa :), y le preguntará al usuario si desea continuar.
    try:
        texto_habilidades = ''
        texto_habilidades,lista_habilidades = retornar_texto("abilities","ability")
        
        texto_movimientos = ''
        texto_movimientos,lista_movimientos = retornar_texto("moves","move")
            
        texto_tipos = ''
        texto_tipos,lista_tipos = retornar_texto("types","type")
        
        # Para mostrar su imagen, peso y tamaño:
        img = pokemon_jason["sprites"]["front_default"]
        imagen = Image.open(urlopen(img))
        plt.subplot(3,3,1)
        plt.imshow(imagen)
        plt.title(f'''Nombre del pokemon: {pokemon_jason["name"].capitalize()}''')
        plt.xlabel(f'''Peso: {pokemon_jason["weight"]}   Tamaño: {pokemon_jason["height"]}''')
        # Para mostrar todos sus movimientos:
        graficar(3,f'''Movmientos de {pokemon_jason["name"].capitalize()}''',texto_movimientos,5)
        # Para mostrar sus habilidades:
        graficar(7,f'''Habilidades de {pokemon_jason["name"].capitalize()}''',texto_habilidades,6)
        # Para mostrar todos sus tipos: 
        graficar(9,f'''Tipos de {pokemon_jason["name"].capitalize()}''',texto_tipos,9)
        
        plt.show()
        diccionario = {
            "Nombre": pokemon_jason["name"].capitalize(),
            "Peso": pokemon_jason["weight"],
            "Tamaño": pokemon_jason["height"],
            "Movimientos": lista_movimientos,
            "Habilidades": lista_habilidades,
            "Tipos": lista_tipos
        }
        lista_diccionarios.append(diccionario)
    except:
        print(f'El pokemon {nombre_pokemon} no existe!')
            
    answer = input('Desea intentar con algún otro pokemon (S/N)? ')
    while(answer != 's' and answer != 'S' and answer != 'n' and answer != 'N'):
        answer = input(f'La respuesta {answer} es ¡INVÁLIDA!, intentelo de nuevo (S/N): ')
    if(answer == ('n' or 'N')):
        print('Gracias por confiar en nosotros, nos vemos la próxima, adios :).')
        for i in lista_diccionarios:
            lista_archivo.append(i)
        file = open('archivo_uno.json','w')
        file.write(json.dumps(lista_archivo))
        file.close()
        exit()
