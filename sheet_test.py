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
import requests

peticion_url = requests.get('https://pokeapi.co/api/v2/pokemon/charizard')

url_json = peticion_url.json()

print(url_json["name"])
# Como mostrar las habilidade de un pokemon con la Poke_Api:
print('\nHABILIDADES DE UN POKEMON: ')
cont = -1
for i in url_json["abilities"]:
    cont += 1
    print(url_json["abilities"][cont]["ability"]["name"])
    
# Como mostrar los movimientos de un pokemon con la Poke_Api:
print('\nMOVIMIENTOS DE UN POKEMON:')
cont = -1
for i in url_json["moves"]:
    cont += 1
    print(url_json["moves"][cont]["move"]["name"])
    
# Como mostrar los types de un pokemon:
print('\nTIPOS DE UN POKEMON: ')
cont = -1
for i in url_json["types"]:
    cont += 1
    print(url_json["types"][cont]["type"]["name"])