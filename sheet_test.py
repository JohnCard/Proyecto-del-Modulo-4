from string import ascii_lowercase,ascii_uppercase
# ---------------------------------------------------------------------------------------------------------

# experimento 1 : pruebas con las palabras clave "True" y "break":

print(' experimento 1 ')
while True:
    answer = input('Ingresar respuesta uno: ')
    if answer == '1':
        break
    elif answer == '2':
        while True:
            answer_dos = input('Ingresar respuesta dos: ')
            if answer_dos == '3':
                break

# conclusión del experimento 1 : ¡Éxitoso!

# ---------------------------------------------------------------------------------------------------------

# experimento 2 : pruebas con returns:

print(' experimento 2 ')
def devolver():
    return 1,2

a,b = devolver()
print(a)
print(b)

# conclusión del experimento 2 : ¡Éxitoso!

# ---------------------------------------------------------------------------------------------------------

# experimento 3 : pruebas con listas:

print(' experimento 3 ')
cont = 15
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in lista:
    cont -= 1
    print(lista[cont])
    
# conclusión del experimento 3 : ¡Éxitoso! 

# ---------------------------------------------------------------------------------------------------------

# experimento 4 : pruebas con archivos:
print(' experimento 4 ')
with open('reto_semana_14.txt','r') as archivo:
    for i in archivo:
        print(i)

# conclusión del experimento 4 : ¡Éxitoso!

# ---------------------------------------------------------------------------------------------------------

# experimento 5 : pruebas con string
print(' experimento 5 ')
print(ascii_uppercase,ascii_lowercase)
print('@' in (f'{ascii_lowercase}'+'@'))

# conclusión del experimento 5 : ¡Éxitoso!

# ---------------------------------------------------------------------------------------------------------

# experimento 6 : pruebas con "or" y "and"

print(' experimento 6 ')
c = 'abc'
print(('a' or 'i') in c)
print(('e' or 'i') in c)

# conclusión del experimento 6 : ¡Éxitoso!

# ---------------------------------------------------------------------------------------------------------

# experimento 7 : pruebas con archivos

print(' experimento 7 ') 
with open("reto_semana_15.txt",'w') as file:
    file.write('Archivo dos')
    
# conclusión del experimento 7 : ¡Éxitoso!

# ---------------------------------------------------------------------------------------------------------

# experimento 8 : pruebas con import
