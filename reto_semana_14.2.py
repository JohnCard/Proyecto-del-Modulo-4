from reto_semana_14 import nombres,telefonos,correos,validar_variable,validar_telefono,abecedario,numeros
from reto_semana_14 import correos_electronicos,validar_respuesta,recorrer

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

# En esta primera parte le preguntamos al usuario que archivo le gustaria abrir para poder ver toda su 
# información contenida por el momento, mostrandole una lista con todos los nombres de los archivos disponibles
# para solicitar información, y mientras no digite exactamente igual el nombre de alguno de ellos, ¡No se le 
# permitirá continuar!, ya que obviamente no puede solicitar información que no existe ya que despues se le 
# pregunbtará si desea hacer alguna modificación.

# esta será la lista con todos los archivos disponibles
archivos = ['archivo_cinco','archivo_cuatro','archivo_tres','archivo_dos','archivo_uno','reto_semana_14',
'reto_semana_15']

# le mostramos la lista junto con una pequeña bienvenida:
print('''
Sea coordialemente bienvenido al programa donde le permitimos modificar datos de los nombres, telefonos o 
correos registrados en el programa anterior  😎 😁 🤠 🧐 🤓 🥸 🤟 🤘 👨‍💻 🧑‍💻 🕵️‍♂️, a continuación, le 
mostraremos una lista con todos los archivos disponibles a solicitar, pero en caso de querer salir del 
programa, solo deberá resionar una "N":
''')
while True:
    indice_archivo = 0
    for archivo in archivos:
        indice_archivo += 1
        print(f'Archivo numero {indice_archivo}: {archivo}')

    # ahora le preguntamos cual de todos los archivos mostrados en el ciclo desea modificar.
    archivo_nombre = input('''Digite el nombre del archivo que desea modificar (debe escribir por lo menos su 
nombre tal y como se muestra en la lista), o salga del programa con un "N": ''')
    while True:
        if(archivo_nombre not in archivos and archivo_nombre != ('n' and 'N')):
            print(f'Este nombre ({archivo_nombre}) ¡NO EXISTE EN LA LISTA!, favor intentarlo de nuevo o slaga con un "N": ')
            indice_archivo = 0
            for archivo in archivos:
                indice_archivo += 1
                print(f'Archivo numero {indice_archivo}: {archivo}')
            archivo_nombre = input('Digite el nombre del archivo que desea modificar (debe escribir por lo menos su nombre tal y como se muestra en la lista): ')
        else:
            break
    if((archivo_nombre.endswith('txt')) == False):
        archivo_nombre = archivo_nombre + '.txt'
    elif(archivo_nombre.endswith('.txt')):
        pass
    
    if(archivo_nombre != ''):
        while True:
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
            answer = validar_respuesta(answer)
            if(answer == ('s' or 'S')):
                while True:
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
                    print('''
                    A continuación, le mostramos los indices de a cuerdo al atributo que se desee modificar:
                    1 - Nombre
                    2 - Télefono
                    3 - Correo
                    ''')
                    while True:
                        print('''
                    1 - Nombre
                    2 - Télefono
                    3 - Correo
                    ''')
                        indice_atributo = input(f'''Digite el indice del atributo que desea modificar de 
            {nombres[indice_usuario]}: ''')
                        indice_atributo = validar_variable('indice',indice_atributo,lista_indices)
                        if(indice_atributo == '1'):
                            nuevo_nombre = ''
                            nuevo_nombre = validar_variable('nombre',nuevo_nombre,abecedario)
                            nombres[indice_usuario] = nuevo_nombre
                        elif(indice_atributo == '2'):
                            nuevo_telefono = ''
                            nuevo_telefono = validar_telefono(nuevo_telefono,numeros)
                            telefonos[indice_usuario] = nuevo_telefono
                        else:
                            nuevo_correo = ''
                            nuevo_correo = validar_variable('correo',nuevo_correo,correos_electronicos)
                            correos[indice_usuario] = nuevo_correo
                        answer = input(f'Desea modificar algun otro atributo de {nombres[indice_usuario]} (S/N)? ')
                        answer = validar_respuesta(answer)
                        if(answer == ('n' or 'N')):
                            break
                    answer = input('Desea modificar la información de algun otro usuario (S/N)? ')
                    answer = validar_respuesta(answer)
                    if(answer == ('n' or 'N')):
                        with open(direccion_archivo,'w') as archivo:
                            cont_dos = 0
                            for nombre in nombres:
                                cont_dos += 1
                                archivo.write(f'''\n
\tUsuario numero {cont_dos}:
Nombre: {nombre} 
Telefono: {telefonos[cont_dos-1]}
Correo electrónico: {correos[cont_dos-1]}
Fecha de registro: {fechas[cont_dos-1]}''')
                        break
        answer = input('Desea verificar otro archivo (S/N)? ')
        answer = validar_respuesta(answer)
    elif((answer or archivo_nombre) == ('n' or 'N')):
        break
