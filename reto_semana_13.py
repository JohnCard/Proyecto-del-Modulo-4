abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
def recorrer_cadena(param):
    cont = 0
    for letra in param:
      if letra not in abc:
        cont += 1
    return cont

' Reto de la semana 13 - Fundamentos python en Ucamp '
'''
Al iniciar el programa, se mostrará un menú con las siguientes opciones:

● Agregar un nuevo alumno (1).

● Ver los alumnos y las calificaciones (2).

● Salir (S).

● Si se decide agregar un nuevo alumno, corroborar que el nombre no esté en blanco.

● Preguntar cuántas calificaciones se quiere agregar.

● Si se ingresa una calificación que no sea de tipo numérico, se pedirá volver a intentar.

● Después de agregar la información de un alumno, volver al menú principal.

● Si se selecciona la opción 2, mostrar en la pantalla la información de cada alumno y el promedio de sus 
calificaciones. Ejemplo: “Laura Ramírez: Promedio 9.5”

● Si se selecciona la opción ‘S’, indicar que se cerrará 
el programa y preguntar si se está seguro de cerrar el programa o no. 

● Recuerda que lo más importante es que nodeberá detenerse la ejecución del programa en caso de ingresar 
valores equivocados.
'''

print('''
      
      
      Hola quetal, te damos nuestra mas sincera bienvenida a este nuevo programa 😁👽.
      Para empezar queremos mostrarte las siguientes opciones de las cuales oprimiras la tecla solicitada 
      de acuerdo a tu necesidad:
      
        ● Agregar un nuevo alumno (1).

        ● Ver los alumnos y las calificaciones (2).

        ● Salir (S).
        
      ''')
lista_nombres = []
calificaciones = []
answer = input('\t Imprima su primer respuesta (S/1/2): ')
while True:
    if(answer != 'S' and answer != 's' and answer != '1' and answer != '2'):
        print('''
      Usted debe seleccionar una de las opciones siguientes de a cuerdo a su necesidad:
        ● Agregar un nuevo alumno (1).

        ● Ver los alumnos y las calificaciones (2).

        ● Salir (S).
              ''')
        answer = input('Digite nuevamente su respuesta (S/1/2): ')
    elif(answer == '1'):
        nombre = input('Digite el nombre del nuevo alumno: ')
        while(recorrer_cadena(nombre) > 0):
            nombre = input('Digite el nombre del nuevo alumno nuevamente: ')
        lista_nombres.append(nombre)
        while True:
            try:
              num_calificaciones = int(input(f'Digite el numero de calificaciones del alumno {nombre}: '))
              break
            except ValueError as error:
                print(f'Ha ocurrido el siguiente error: {error}')
        cont = 0
        for calificacion in range(num_calificaciones):
            cont+= 1
            calificaciones.append([])
            while True:
                try:
                  calificacion = float(input(f'Digite la calificacion numero {cont}: '))
                  break
                except ValueError as error_dos:
                    print(f'¡Ha digitado mal la calificación numero {cont}!. ')
            calificaciones[0].append(calificacion)
    elif(answer == '2'):
        for nombre in lista_nombres:
            nota_sumatoria = 0
            for nota in calificaciones[calificaciones.index(nombre)]:
                nota_sumatoria += nota
            #### ¡PENDIENTE de las 3:21 p.m.!
            print(f'''
            Nombre del alumno: {nombre}
            Promedio de {nombre}: 
            ''')
    elif(answer == ('s' or 'S')):
        answer_dos = input('Esta seguro de que desea salir del programa (S/N)? ')
        while True:
            if(answer_dos != ('s' and 'S' and 'N' and 'n')):
              answer_dos = input('Digite nuevamente su respuesta (S/N): ')
            else:
              break
    elif(answer_dos == ('s' or 'S')):
      break
