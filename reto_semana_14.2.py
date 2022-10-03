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

# Función 1 : mostrar_archivo()
def mostrar_archivo():
    with open("reto_semana_15.txt",'a') as file:
        for linea in file:
            print(linea)
            