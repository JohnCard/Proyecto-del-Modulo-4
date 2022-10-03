from hashlib import new


file_one = open('archivo_uno.txt','w') # w = write, que es el parametro indica que sobreescribe el archivo
# se le otorga el permiso de sobreescribirle cadenas de texto 
file_one.write('Hola EDteam! :> :> ') # output: 16 que es el no de caracteres que se escribieron en el
# parametro del metodo .write(---)
file_one.close() # .close() que sirve para cerrar el archivo

file_one = open('archivo_uno.txt','w')
file_one.write('Volvemos ha sobreescribir en el archivo')
file_one.close()

# ahora vamos con el metodo .read():
file_dos = open('archivo_uno.txt','r') # el parametro r, que lo unico que otorga es el permiso para leer un 
# archivo txt
print('\nlinea 17_18')
print(file_dos.read())
print('linea 17_18')
file_dos.close()

print('\nlinea 23_24')
print(file_one)
print(file_dos)
print('linea 23_24')

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

# sentencias "with" y "as"

file_tres = open('archivo_dos.txt','r')
print('\nlinea 36_38')
print(file_tres.closed)
file_tres.close()
print(file_tres.closed)
print('linea 36_38')

print('\nlinea 42_44')
with open('archivo_dos.txt','r') as file_tres_dos:
    print(file_tres_dos.closed)
print(file_tres.closed)
print('linea 42_44')

print('\n linea 52')
with open('archivo_dos.txt','a') as file_uno: # a = append (agreaga) que significa agregar al final 
# del archivo
    file_uno.write('\nPrimer file 2')
    file_uno.write('\nPrimer file 3')
    file_uno.write('\nPrimer file 3.5')
    file_uno.write('\nPrimer file 4')
with open('archivo_dos.txt','r') as file_dos:
    print(file_dos.read())
print('linea 52')

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

# asignarle contenido de un archivo a una variable:

# para esto crearemos un nuevo archivo llamado "archivo_tres.txt" en nuestra carpeta de SEMANA_14
with open('archivo_tres.txt','r') as new_file:
    file_four = new_file.read()
    print(f'****{file_four}***')
    
    # esta nueva asignación ya no será posible porque en de la linea 64-65 ya consumimos toda la información
    # del archivo
    file_four = new_file.read()
    print(f'****{file_four}****')

# para lo anterior tendriamos que hacer lo siguiente:
with open('archivo_tres.txt','a') as new_file:
    new_file.write('Nuevo contenido for the letter! ')
with open('archivo_tres.txt','r') as new_file:
    file_four = new_file.read()
    print(f'****{file_four}***')
    
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

# lectura de archivos linea por linea:

# para esto crearemos un nuevo archivo llamado archivo_cuatro.txty luego continuamos
with open('archivo_cuatro.txt','r') as f_lectura:
    no_lines = 0
    for i in f_lectura:
        no_lines += 1
        print(f'Linea {no_lines}: {i}')
    print(f'El archivo tiene {no_lines} lineas. ')

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

# creando una lista a partir de un archivo:
# esto lo realizaremos con el mismo archivo_cuatro.txt:

with open('archivo_cuatro.txt','r') as f_archivo:
    lista_file = f_archivo.readlines()
    print(lista_file)
    
lista_file[1] = 'asignación numero uno'
lista_file.insert(2,'asignación numero dos')
print(lista_file)

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

# ahora vamos a agregarle el contenido de un archivo anteriormente hecho a uno nuevo, el cual llamaremos
# "archivo_cinco":

with open('archivo_cinco.txt','w') as f_archivo:
    f_archivo.writelines(lista_file)
    print(f_archivo)
    
with open('archivo_cinco.txt','r') as f_archivo:
    print(f_archivo.read())