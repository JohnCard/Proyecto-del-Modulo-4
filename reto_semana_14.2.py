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

# En esta primera parte le preguntamos al usuario que archivo le gustaria abrir para poder ver toda su información
# contenida por el momento, mostrandole una lista con todos los nombres de los archivos disponibles para 
# solicitar información, y mientras no digite exactamente igual el nombre de alguno de ellos, ¡No se le permitirá 
# continuar!.            