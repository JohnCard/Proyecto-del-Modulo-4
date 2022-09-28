abc = 'abcdefghijklmñnopqrstuvwxyzABCDEFGHIJKLMÑNOPQRSTUVWXYZ '
def recorrer_cadena(param):
  cont = 0
  for letra in param:
    if letra not in abc:
      cont += 1
  return cont

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

# esta variable (cont_dos - linea 22) la inicializaremos en 0, y para cuando inicie el programa de abajo, ira sumandose de uno en uno cada que el usuario escoja la opción "1" (cada que answer se 
# iguale a 1), ya que si escoje la opción 1, por ende dará a entender que quiere registrar un nuevo nombre y calificaciones nuevas de un alumno, entonces, con eso queremos dar a entender que por ende 
# esta variable tendria por logica la cantidad de alunnos que se tendrán en total al final de la ejecución del  programa cuando el usuario decida terminar de digitar nombres o 
# calificaciones, pero, para que?, bueno, sucede que de acuerdo a como se le valla aumentando un uno a esta variable, será justo el nuevo valor del cont_dos lo que tomaremos de 
# referencia para indicarle la nueva posición ala que ingresaremos la nueva lista de notas del nuevo alumno en la lista calificaciones de la linea 20
cont_dos = 0
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
    # a partir de aqui hasta la linea 58 va la lógica que permitirá al usuario registrar un nuevo nombre y las calificaciones de otro alumno dsitinto
    cont_dos += 1
    nombre = input('Digite el nombre del nuevo alumno: ')
    while(recorrer_cadena(nombre) > 0 or nombre == ''):
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
      calificaciones[cont_dos-1].append(calificacion)
    print('''
  Digite la nueva acción a realizar :
  ● Agregar un nuevo alumno (1).

  ● Ver los alumnos y las calificaciones (2).

  ● Salir (S)
          ''')
    answer = input('Digite su respuesta (S/1/2): ')
    # a partir de aqui si la variable legase a cambiar su valor por un 2, segun los requisitos, nos pide que escribamos la logica para que de esa forma se le muestre al usuario
    # los nombres de los alumnos y los promedios de cada uno, y esta parte del codigo esta hecha de tal manera que que conforme avance el sistema, mostrará los nombres y los 
    # promedios que se lleve registrados hasta ahora de las variables de tipo lista (lista_nombres y calificaciones) declaradas en las lineas 19 y 20 
  elif(answer == '2'):
    alumno = -1
    print('Nombres y promedios de alumnos registrados hasta ahora: ')
    for nombre in lista_nombres:
      alumno += 1
      nota_sumatoria = 0
      for nota in calificaciones[alumno]:
        nota_sumatoria += nota
      promedio = nota_sumatoria/len(calificaciones[alumno])
      print(f'''
      Nombre del alumno {alumno+1}: {nombre}
      Promedio de {nombre}: {promedio}''')
    print('''
  Digite la nueva acción a realizar :
  ● Agregar un nuevo alumno (1).

  ● Ver los alumnos y las calificaciones (2).

  ● Salir (S)
          ''')
    answer = input('Digite su respuesta (S/1/2): ')
  elif(answer == 's' or answer == 'S'):
    answer_dos = input('Esta seguro de que desea salir del programa (S/N)? ')
    while(answer_dos != 's' and answer_dos != 'S' and answer_dos != 'n' and answer_dos != 'N'):
      answer_dos = input('Digite nuevamente su respuesta (S/N): ')
    if(answer_dos == 's' or answer_dos == 'S'):
      break
    else:
      print('''
  Digite la nueva acción a realizar :
  ● Agregar un nuevo alumno (1).

  ● Ver los alumnos y las calificaciones (2).

  ● Salir (S)
          ''')
      answer = input('Digite su respuesta (S/1/2): ')
