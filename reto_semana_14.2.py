from reto_semana_14 import nombres,telefonos,correos

# ejercicio del reto_semanal_14
'''
En el ejercicio anterior, solo vimos una parte: cómo escribir un nuevo archivo para guardar nuestras salidas. 
Ahora, como reto, te propongo que hagas un programa en el que abras el archivo generado en el ejercicio 
anterior y puedas modificar los datos de algún contacto. 
● El programa te mostrará en la pantalla la información de los contactos guardados numerada. 
● Preguntará de cuál de los contactos se desea modificar la información.
● Se podrá modificar el nombre, el teléfono y el correo. 
● Se debe actualizar la información en el archivo.
● El programa no debe interrumpirse al ingresar mal los datos o las opciones.
'''

# inicialización de funciones:

# Función 1 : mostrar_archivo(archivo)
def mostrar_archivo(archivo):
    '''
    Esta función recibe como parametro un archivo, el cual como se muestra a continuación, se usa el método
    "with" para abrirlo y mostrar su información en un ciclo "for"
    '''
    with open(archivo,'a') as file:
        for linea in file:
            print(linea)

# inicialización de listas o variables a utilizar:

# esta la usaremos para cuando toque preguntarle al usuario que atributo le gustaria modificar del usuario 
# solicitado, evitando que digite algo diferente al nombre de un atributo
usuarios_atributos = ['1','2','3']

# En esta primera parte le preguntamos al usuario que archivo le gustaria abrir para poder ver toda su información
# contenida por el momento, mostrandole una lista con todos los nombres de los archivos disponibles para 
# solicitar información, y mientras no digite exactamente igual el nombre de alguno de ellos, ¡No se le permitirá 
# continuar!, ya que obviamente no puede solicitar información que no existe ya que despues se le pregunbtará si 
# desea hacer alguna modificación.

# esta será la lista con todos los archivos disponibles
archivos = ['archivo_cinco','archivo_cuatro','archivo_tres','archivo_dos','archivo_uno','reto_semana_14','reto_semana_15']

# le mostramos la lista junto con una pequeña bienvenida:
print('''
Sea coordialemente bienvenido al programa donde le permitimos modificar datos de los nombres, telefonos o correos 
registrados en el programa anterior  😎 😁 🤠 🧐 🤓 🥸 🤟 🤘 👨‍💻 🧑‍💻 🕵️‍♂️, a continuación, le mostraremos
una lista con todos los archivos disponibles a solicitar:
''')
while True:
    indice_archivo = 0
    for archivo in archivos:
        indice_archivo += 1
        print(f'Archivo numero {indice_archivo}: {archivo}')

    # ahora le preguntamos cual de todos los archivos mostrados en el ciclo desea modificar.
    archivo_nombre = input('Digite el nombre del archivo que desea modificar (debe escribir por lo menos su nombre tal y como se muestra en la lista): ')
    while True:
        if(archivo_nombre not in archivos):
            print(f'Este nombre ({archivo_nombre}) ¡NO EXISTE EN LA LISTA!, favor intentarlo de nuevo: ')
            indice_archivo = 0
            for archivo in archivos:
                indice_archivo += 1
                print(f'Archivo numero {indice_archivo}: {archivo}')
            archivo_nombre = input('Digite el nombre del archivo que desea modificar (debe escribir por lo menos su nombre tal y como se muestra en la lista): ')
        else:
            break
    if((archivo_nombre.endswith('txt')) == False):
        archivo_nombre = archivo_nombre + '.txt'
    else:
        pass

    # ahora, de acuerdo al archivo solicitado por el usuario, tomamos el nombre como referencia para 
    # abrirlo con un "with", hacer un recorrido por el y consumir toda su información (nombres, 
    # telefonos y correos) para ser guardados en las listas nombres, telefonos y correos importados 
    # en la "linea 1 del codigo", al igual que cualquier otra cosa que vallamos a necesitar:
    with open(archivo_nombre,'r') as file:
        # declaramos esta variable que al final del ciclo, terminará con la cantidad de todos los usuarios disponibles
        indices = 0
        for linea in file:
            if('Nombre' in linea):
                nombres.append(linea[8:])
            elif('Telefono' in linea):
                telefonos.append(linea[10:])
            elif('Correo' in linea):
                correos.append(linea[20:])
            elif('Usuario' in linea):
                indices += 1
    
    # creamos una lista con los indices de los usarios disponibles en el archivo
    lista_indices = []
    for indice in range(indices):
        lista_indices.append(str(indice+1))

    # ahora le mostramos todo el contenido del archivo solicitado por el usuario
    with open(archivo_nombre,'r') as file:
        print(file.read())
    
    # le preguntamos si desea solicitar la información de algún usuario antes que nada
    answer = input('Desea modificar la información de algun usuario (S/N): ')
    while(answer != ('s','S','n','N')):
        answer = input(f'La respuesta {answer} ¡NO ES VÁLIDA!, favor de intentarlo de nuevo (S/N): ')
    if(answer == ('s' or 'S')):
        print('Usuarios disponibles: ⤵⬇📄📃📜')
        cont = 0
        for nombre in nombres:
            cont += 1
            print(f'Usuario numero {cont}: {nombre}')
        indice_usuario = input('Digite el indice del usuario de quien desea modificar los atributos: ')
        while(indice_usuario not in lista_indices):
            print(f'El indice de usuario {indice_usuario} ¡NO EXISTE!, favor de intentarlo de nuevo: ')
            cont = 0
            for nombre in nombres:
                cont += 1
                print(f'Usuario numero {cont}: {nombre}')
            indice_usuario = input('Digite el indice del usuario de quien desea modificar los atributos: ')
        # print --- ¡PENDIENTE! ---
    else:
        answer_final = input('Desea checar algun otro archivo (S/N)? ')
        while(answer_final != ('s','S','n','N')):
            answer_final = input(f'La respuesta {answer} ¡NO ES VÁLIDA!, favor de intentarlo de nuevo (S/N): ')
    if(answer_final == ('N' or 'n')):
        break