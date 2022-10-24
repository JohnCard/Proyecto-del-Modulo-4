import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen
import json

def graficar(posicion,mensaje,mensaje_ylabel,texto,font_size):
    '''
    Esta función recibe como parametro la posicion, un mensaje, el texto y el font_size para que especificamente a
    partir de la linea de codigo de la 90 a la 94, esta sea usada para mostrar una imagen con matplotlib 
    con todos los textos especiificados como parametros que tendràn la información correspondiente a su contexto (mensaje)
    comentado una linea antes de ser usada esta función.
    '''
    plt.subplot(4,4,posicion)
    plt.axis([0,20,5,0])
    plt.title(mensaje)
    plt.ylabel(mensaje_ylabel)
    plt.text(0.5,4.9,texto,fontsize=font_size)

def retornar_texto(atributo,atributo_dos):
    '''
    Como bien lo dice su nombre, esta función retorna un texto de acuerdo a lo que hace su algoritmo, recibiendo 2 
    parametros, el atributo que indicará cual parte del objeto json se va ha evaluar y el atributo_dos que serà 
    una parte mas interna perteneciente a uno de los atributos dela lista atributo en el objeto json, asi como 
    también retornará finalmente una lista con los valores que corresponden al contexto dela propiedad del objeto
    '''
    cont = 0
    texto = ''
    lista_atributo = []
    # aqui el atributo es efectivamente uno de los atributos o propiedades del objeto json solicitado por el get
    if(cont+5 > len(pokemon_jason[f"{atributo}"])):
        cont = -1
        for i in pokemon_jason[f"{atributo}"]:
            cont += 1
            # y el atributo_dos es también uno de los atributos del subobjeto atributo
            texto += pokemon_jason[f"{atributo}"][cont][f"{atributo_dos}"]["name"]+', '
            lista_atributo.append(pokemon_jason[f"{atributo}"][cont][f"{atributo_dos}"]["name"])
    else:
        cont = 0
        texto = ''     
        texto_dos = ''   
        while(cont < len(pokemon_jason[f"{atributo}"])):
            if(cont+5 > len(pokemon_jason[f"{atributo}"])):
                texto_dos = ''
                for i in range(cont,len(pokemon_jason[f"{atributo}"])):
                    texto += pokemon_jason[f"{atributo}"][i][f"{atributo_dos}"]["name"]+', '
                    texto_dos += pokemon_jason[f"{atributo}"][i][f"{atributo_dos}"]["name"]+', '
                lista_atributo.append(texto_dos)
            else:
                texto_dos = ''
                for i in range(cont,cont+5):
                    texto += pokemon_jason[f"{atributo}"][i][f"{atributo_dos}"]["name"]+', '
                    texto_dos += pokemon_jason[f"{atributo}"][i][f"{atributo_dos}"]["name"]+', '
                texto += '\n';lista_atributo.append(texto_dos)
            cont += 5
    return texto + 'etc.',lista_atributo

# aqui lo que se pretende es abrir un archivo json para guardar toda su información en una variable 
file = open('archivo_uno.json','r')
lista_archivo = json.loads(file.read())
file.close()

answer = 's'
lista_diccionarios = []
while(answer == ('s' or 'S')):
    nombre_pokemon = input('Digite el nombre del pokemon a consultar: ').lower()
    url_peticion = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}')
    
    # primero intentaremos obtener el json de la petición si la petición dio un "200", como tanto 
    # esperariamos, para proseguir con las demas instrucciones
    try:
        # empezamos por crear el json del objeto requests
        pokemon_jason = url_peticion.json()

        # y despues de acuerdo a todos sus datos, obtenemos lo que son el peso, el tamaño, el nombre, movimientos,
        # habilidades y tipos del pokemon:
        
        texto_habilidades = ''
        texto_habilidades,lista_habilidades = retornar_texto("abilities","ability")
        
        texto_movimientos = ''
        texto_movimientos,lista_movimientos = retornar_texto("moves","move")
            
        texto_tipos = ''
        texto_tipos,lista_tipos = retornar_texto("types","type")
        
        # Para mostrar su imagen, peso y tamaño:
        img = pokemon_jason["sprites"]["front_default"]
        imagen = Image.open(urlopen(img))
        plt.subplot(4,4,1)
        plt.imshow(imagen)
        plt.title(f'''   Nombre del pokemon: {pokemon_jason["name"].capitalize()}''')
        # Usamos el xlabel especificamente para mostrar el peso y tamaño del pokemon 
        plt.xlabel(f'''Peso: {pokemon_jason["weight"]}   Tamaño: {pokemon_jason["height"]}''')
        # Para mostrar todos sus movimientos:
        graficar(7,'',f'''Movmientos de {pokemon_jason["name"].capitalize()}''',texto_movimientos,5)
        # Para mostrar sus habilidades:
        graficar(13,f'''Habilidades de {pokemon_jason["name"].capitalize()}''','',texto_habilidades,6)
        # Para mostrar todos sus tipos: 
        graficar(16,f'''Tipos de {pokemon_jason["name"].capitalize()}''','',texto_tipos,9)
        
        plt.show()
        # aqui crearemos un nuevo diccionario que llevará toda la nueva información del pokemon que halla 
        # sido solicitado por el usuario
        diccionario = {
            "Nombre": pokemon_jason["name"].capitalize(),
            "Peso": pokemon_jason["weight"],
            "Tamaño": pokemon_jason["height"],
            "Movimientos": lista_movimientos,
            "Habilidades": lista_habilidades,
            "Tipos": lista_tipos,
            "Foto-Pokemon": pokemon_jason["sprites"]["front_default"]
        }
        # y en la variable lista_diccionarios donde se guardo toda la información del objeto json, anteriormente abierto,
        # la empezamos a actualizar con la nueva información que se valla obteniendo por cada pokemon que el usuario
        # consulte
        lista_diccionarios.append(diccionario)
    except:
        print(f'La petición no funcionó. !')
        
    answer = input('Desea intentar con algún otro pokemon (S/N)? ')
    while(answer != 's' and answer != 'S' and answer != 'n' and answer != 'N'):
        answer = input(f'La respuesta {answer} es ¡INVÁLIDA!, intentelo de nuevo (S/N): ')
    if(answer == ('n' or 'N')):
        print('Gracias por confiar en nosotros, nos vemos la próxima, adios :).')
        for i in lista_diccionarios:
            lista_archivo.append(i)
        file = open('archivo_uno.json','w')
        file.write(json.dumps(lista_archivo,indent=1))
        file.close()
        exit()