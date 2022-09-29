import matplotlib.pyplot as plt

# inicializamos con esta variable yaque será la que contenga los caracteres permitidos en los nombres 
# que se digiten en el programa
abc = 'abcdefghijklmñnopqrstuvwxyzABCDEFGHIJKLMÑNOPQRSTUVWXYZ '

def recorrer_cadena(param):
  '''
  esta función recibirá un param, el cual hará referencia a una cadena digitada por el usuario, lo que hará
  esta función será recorrer esa cadena (param), con el cilo for que tiene para revisar cada una de sus 
  caracteres y asegurarse de que ninguno sea inexistente en la variable abc, yaque de ser asi, se le 
  aumentará un uno a la variable cont, que contará como tal cuantas variables no permitidas hay, aunque
  de hecho basta con que cuente solo una para darse cuenta de que hay un error en el parametro o cadena
  '''
  cont = 0
  'recorremos el parametro o cadena del usuario'
  for letra in param:
    'detectamos un dato erroneo!'
    if letra not in abc:
      cont += 1
  'si llega a lanzar algo mayor a 0, significa que algo se digito mal, si no, entonces será igual a 0'
  return cont

print('''
  Hola quetal, te damos nuestra mas sincera bienvenida a este nuevo programa 😁👽.
  Para empezar queremos mostrarte las siguientes opciones de las cuales oprimiras la tecla solicitada 
  de acuerdo a tu necesidad:
  ● Agregar un nuevo alumno (1).

  ● Ver los alumnos y las calificaciones (2).

  ● Salir (S).     
''')
# en esta lista, durante la ejecución del programa, será a la que se le asignen los nombres de cada nuevo
# alumno
lista_nombres = []
# en esta lista, durante la ejecución del programa, será a la que se le vallan asignando nuevas listas 
# en las cuales, por cada una, se le asignarán las calificaciones de cada alumno
calificaciones = []

# inicializaremos también esta lista de promedios para una pequeña practica de grafica de barras al final
# del reto de la semana, una lista donde durante el transcurso del programa, agregaremos los promedios
#  de cada alumno en esta lista👽😁🕸
promedios = []

# esta variable (cont_dos - linea 22) la inicializaremos en 0, y para cuando inicie el programa de abajo, ira 
# sumandose de uno en uno cada que el usuario escoja la opción "1" (cada que answer se iguale a 1), ya que si 
# escoje la opción 1, por ende dará a entender que quiere registrar un nuevo nombre y calificaciones nuevas de 
# un alumno, entonces, con eso queremos dar a entender que por ende esta variable tendria por logica la 
# cantidad de alunnos que se tendrán en total al final de la ejecución del  programa cuando el usuario decida 
# terminar de digitar nombres o calificaciones, pero, para que?, bueno, sucede que de acuerdo a como se le 
# valla aumentando un uno a esta variable, será justo el nuevo valor del cont_dos lo que tomaremos de 
# referencia para indicarle la nueva posición ala que ingresaremos la nueva lista de notas del nuevo alumno en 
# la lista calificaciones de la linea 20
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
    # a partir de aqui hasta la linea 58 va la lógica que permitirá al usuario registrar un nuevo nombre y las
    # calificaciones de otro alumno dsitinto
    cont_dos += 1
    nombre = input(f'Digite el nombre del nuevo alumno numero {cont_dos}: ')
    while(recorrer_cadena(nombre) > 0 or nombre == ''):
      nombre = input('Digite el nombre del nuevo alumno nuevamente: ')
    lista_nombres.append(nombre)
    while True:
      try:
        num_calificaciones = int(input(f'Digite el numero de calificaciones del alumno {nombre}: '))
        break
      except ValueError as error:
        print(f'Ha ocurrido el siguiente error: {error}')
    calificaciones.append([])
    cont = 0
    for calificacion in range(num_calificaciones):
      cont+= 1
      while True:
        try:
          calificacion = float(input(f'Digite la calificacion numero {cont}: '))
          break
        except ValueError as error_dos:
          print(f'¡Ha digitado mal la calificación numero {cont}!. ')
      calificaciones[cont_dos-1].append(calificacion)
    nota_sumatoria = 0
    for nota in calificaciones[cont_dos-1]:
      nota_sumatoria += nota
    promedio = nota_sumatoria/len(calificaciones[cont_dos-1])
    promedios.append(promedio)
    print('''
  Digite la nueva acción a realizar :
  ● Agregar un nuevo alumno (1).

  ● Ver los alumnos y las calificaciones (2).

  ● Salir (S)
          ''')
    answer = input('Digite su respuesta: ')
    # a partir de aqui si la variable legase a cambiar su valor por un 2, segun los requisitos, nos pide que 
    # escribamos la logica para que de esa forma se le muestre al usuario los nombres de los alumnos y los 
    # promedios de cada uno, y esta parte del codigo esta hecha de tal manera que que conforme avance el 
    # sistema, mostrará los nombres y los promedios que se lleve registrados hasta ahora de las variables de 
    # tipo lista (lista_nombres y calificaciones) declaradas en las lineas 19 y 20
  elif(answer == '2'):
    alumno = -1
    print('Nombres y promedios de alumnos registrados hasta ahora: ')
    for nombre in lista_nombres:
      alumno += 1
      # nota_sumatoria = 0
      # for nota in calificaciones[alumno]:
      #   nota_sumatoria += nota
      # promedio = nota_sumatoria/len(calificaciones[alumno])
      print(f'''
      Nombre del alumno {alumno+1}: {nombre}
      Promedio de {nombre}: {promedios[alumno]: .3f}''')
    print('''
  Digite la nueva acción a realizar :
  ● Agregar un nuevo alumno (1).

  ● Ver los alumnos y las calificaciones (2).

  ● Salir (S)
          ''')
    answer = input('Digite su respuesta: ')
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
      answer = input('Digite su respuesta: ')
      
# Una pequeña practica extra 😁😎👽🧐🤠🤓 con matplotlib.pyplot con los nombres de cada alumno y sus 
# correspondientes promedios

plt.bar(lista_nombres,promedios,color='#4CAF50')
plt.title('Nombres vs Promedios', loc='right')
plt.xlabel('Nombres de los Alumnos')
plt.ylabel('Promedios correspondientes')
plt.grid(axis='y', linestyle = '--',linewidth='2')
plt.show()
