# funciones para el programa

# 1 .- Función: mostrar_menu()
def mostrar_menu():
    '''
    esta función, al ser llamada mostrará las opciones disponibles a realizar al inició del programa
    '''
    print('''
    Digite la siguiente acción a realizar: 
    1 para registrar un usuario
    2 para dejer de registrar usuarios y poder salir del programa
          ''')
    
# 2 .- Función: respuesta(answer)
def respuesta(answer):
    'Esta función ayudará a que el usuario no digite nada diferente de la opción 1 ó 2'
    answer = input('\t Digite su respuesta (1/2): ')
    while(answer != '1' and answer != '2'):
        answer = input(f'La respuesta {answer} ¡NO ES VÁLIDA!, intentelo de nuevo (1/2): ')
    return answer

# 3 .- Función: recorrer(cadena,variable)
def recorrer(cadena,variable):
    '''
    esta función ayudará a recorrer el parametro "cadena", y si en su ciclo for detecta una letra que no exista 
    en parametro "variable", entonces se le aumentará un uno a su contador dando a entender que hay ¡ERRORES!
    '''
    cont = 0
    for dato in cadena:
        if dato not in variable:
            cont += 1
    return cont

# 4 .- Función: validar_variable(cadena,variable)
def validar_variable(tipo_dato,cadena,variable):
    '''
    esta función resive el parametro tipo_dato para darle a entender al usuario que se le pide en el input,
    y luego de que el lo introduzca, en caso de haber introducido algo mal, se inicializará un ciclo que 
    no terminará hasta que digité bien el parametro con ayuda de la función "recorrer()"
    '''
    cadena = input(f'Digite su {tipo_dato}: ')
    while(recorrer(cadena,variable) > 0 or ('..' or '@@') in cadena):
        cadena = input(f'El dato {cadena} ¡NO ES VÁLIDO!, digite su {tipo_dato} de nuevo por favor: ')
    return cadena

# 5 .- Función: registrar_usuarios()
def registrar_usuarios():
    '''
    Empezaremos creando una función que nos permitirá efectivamente crear usuarios con los 
    siguientes atributos: 
    nombre, teléfono y correo:
    '''
    while True:
        mostrar_menu()
        answer = ''
        answer = respuesta(answer)
        if answer == '1':
            # inicilizamos cada variable (nombre,telefono y correo) con un '' devido al error siguiente:
            # UnboundLocalError: local variable 'nombre' referenced before assignment
            # ya que si solo le asignamos la llamada de la función (validar_variable()), nos marcaría ese error
            
            nombre = ''
            nombre = validar_variable('nombre',nombre,abecedario)
            nombres.append(nombre)
            telefono = ''
            telefono = validar_telefono(telefono,numeros)
            telefonos.append(telefono)
            correo = ''
            correo = validar_variable('correo electrónico',correo,correos_electronicos)
            correos.append(correo)
        else:
            break

# 7 .- Función: validar_variable(cadena,variable)
def validar_telefono(numero,variable):
    '''
    en caso de haber introducido algo mal en su numero telefonico (numero), se inicializará un ciclo que 
    no terminará hasta que digité bien el parametro con ayuda de la función "recorrer()"
    '''
    numero = input(f'''Digite su numero telefonico (con espacios(" ") o guiones(-)): ''')
    while(recorrer(numero,variable) > 0 or len(numero) > 12 or len(numero) < 12):
        numero = input(f'El dato {numero} ¡NO ES VÁLIDO!, digite su numero telefonico de nuevo por favor: ')
    return numero

# este es un apartado donde declararemos variables que pueden resultar utiles para validar datos de un 
# usuario nuevo:

# esta variable nos puede servir porque están solo los caracteres que deberían contener los nombres
abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ abcdefghijklmnñopqrstuvwxyz'

# esta variable nos puede servir porque están solo los caracteres que deberían contener los numeros 
# telefonicos
numeros = '123456789- '

# estas serán las listas que contendrán los distintos nombres, telefonos u correos de cada usuario registrado
# cuando en el transcurso del programa en las lineas 66,69,72 toque agregarles los datos con el metodo
# append():
nombres = []
telefonos = []
correos = []
# esta variable nos puede servir porque están solo los caracteres que deberían contener los correos
# electronicos
correos_electronicos = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz@.123456789-'
        
# ahora solo llamamos a la función registrar_usuarios():
print('''
    Bienvenido, en este programa usted podrá registrar distintos ususarios, cada uno soló requerirá de su        
    nombre, correo y telefono para ser validado, usted soló debe ingresar uno de los numeros que se le van       
    a mostrar a continuación de acuerdo a su necesidad
      ''')
registrar_usuarios()

        
# la lógica final de este programa consistirá en agregar todos los nombres, telefonos y correos electronicos
# digitados en las listas nombres,telefonos y correos en el archivo "reto_semana_14.txt":

# en esta parte del codigo lo que pretenderemos será abrir el archivo que esta enlazado con el reto de la 
# semana, donde por cada usuario ya registrado en caso de que este programa ya haya sido usado anteriormente,
# lo que haremos será abrir un contador el cual por cada que se encuentre con la alabra "Usuario", por ende se
# estará encontrando con un usuario nuevo, y ahi se le sumará un uno, para que en la parte de la linea 123
# donde empezamos a agregarle al archivo "reto_semana_14.txt" todos los nombres,telefonos y correos nuevos
# con el formato especificado que se puede ver ahi, a parte de Usuario numero {cont}, lo haga con un indice
# correcto
with open("reto_semana_14.txt",'r') as file:
    cont = 0
    for i in file:
        if 'Usuario' in i:
            cont += 1
            
with open("reto_semana_14.txt",'a') as archivo:
    cont_dos = 0
    for nombre in nombres:
        cont_dos += 1
        cont += 1
        archivo.write(f'''\n
\tUsuario numero {cont}:
Nombre: {nombre}
Telefono: {telefonos[cont_dos-1]}
Correo electrónico: {correos[cont_dos-1]}''')

# Ahora iremos con la siguiente parte del programa