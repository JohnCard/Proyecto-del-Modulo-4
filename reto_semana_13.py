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
    answer = input('Digite su respuesta: ')
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
