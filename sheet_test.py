from string import ascii_lowercase,ascii_uppercase
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
import requests
from PIL import Image
from urllib.request import urlopen
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

# ---------------------------------------------------------------------------------------------------------

# experimento 9 : pruebas con listas
# experimento 9.1:
lis = []
for i in range(30):
    lis.append((i+1))
print(lis)
u = 0; string = ''
while(u<len(lis)):
    for i in range(u,u+5):
        i+= 1
        string += str(i) + ' '
    u += 5
print(string)
# Conclusión: ¡Funcionó!
    
# experimento 9.2:
for i in range(5,7):
    print(i)
# Conclusión: ¡Funcionó!
    
# experimento 9.3: 
a = 'Hola mundo\nquetal como andas'
b = 'a\n'
print('\n' in (b))
# conclusion: ¡Funcionó!

# ---------------------------------------------------------------------------------------------------------

# experimento 10 : pruebas con matplotlib
fig = plt.figure()
plt.axis([0, 20, 0, 20])
plt.text(1, 1, 'Hola mundo \n como andas', ha='left', rotation=0)
plt.show()

lis = []
for i in range(30):
    lis.append((i+1))

u = 0; string = ''
while(u<len(lis)):
    for i in range(u,u+5):
        i+= 1
        string += str(i) + ' ' +'\n'
    u += 5

fig = plt.figure()
plt.axis([0, 20, 0, 20])
plt.text(1, 1, string, ha='left', rotation=0)
plt.show()

# -------------------------------------------------------------------------
# 3:03 p. m. 22/10/2022
import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen
import json

url_peticion = requests.get(f'https://pokeapi.co/api/v2/pokemon/ditto')
json_url = url_peticion.json()
# img = pokemon_jason["sprites"]["front_shinny"]
# imagen = Image.open(urlopen(img))
# plt.title(pokemon_jason["name"])
# plt.imshow(imagen)
imagen = json_url["sprites"]["front_default"]
img = Image.open(urlopen(imagen))
# plt.title(f'''Nombre: {json["name"]}''')
var = 'Hello everyone'
for i in range(2):
    var += 'Hola'
plt.xlabel(f'South park es lo mejor\también cartman\n{var}')
plt.imshow(img)
plt.show()

# file = open('archivo_uno.json','a')
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# file.write(json.dumps(x))
# file.close()
file = open('archivo_uno.json','r')
x = json.loads(file.read())
print(x,type(x))
print(type(file.read()))
# lista_archivo = json.loads(file.read())
file.close()

# Movimiento numero 124: scor
cadena = 'Movimiento numero 124: scor'
print(len(cadena)) # OutPut: 27

# experimento nuevo: 
def retornar():
    return 1,2
a,b = retornar()
print(a,b)

file = open('archivo_uno.json','w')
lista = x
file.write(str(lista))
file.close()
