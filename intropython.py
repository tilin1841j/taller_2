# while
# while <condicon_verdadera>:
#      cuerpo del ciclo
#condiciones son: expresiones booleanas (or, and) y operaciones de comparación
# ciclos controlados por un contador enteros
# ciclos controlados por un evento 

import random

i=0
k=0

while 1==1:
   print("ciclo")
    #importante modificar el valor del contador 
i+1
    
a=0

while a !=5:
    a= random. randint(1,10)
    print(a)
    
print("se acabo")
    
    
a=0
while 1==1:
    
    a=int(input("ingrese un numero"))
    
    if a==10:
        break
    
# for: se utillizar para recorrer un "iterable"
# lista, tupla, diccionario...

#lista: conjunto de variables organizadas en 
# espacios consecutivos de memoria. A las que 
# se les asigna un unico nombre. se diferencian
#por la posicion que ocupan rerspecto al primer
#elemento de lista

miLista = [1, True, "textos", 3.89]
miLista2 = []

print(miLista)
print(miLista2)

# en python todos son objetos.

print(miLista)
miLista.append(45)
print(miLista)


print(len(miLista))

#tupla: lista inmutable

miTupla=(2,45,6,8,9,10)

# for: ciclo para recorrr iterables. El cuerpo
# se repite tantas veces como elemento tenga el 
# iterable. En cada ciclo se guarda el valor

miLista=[5,45,89,6,7]

#EStrucutra del for en python:
# for <variable_donde_guardo_el_elemento in iterable:

for x in miLista:
    print(x)
    if x>50:
        print("grande")
        
# si solo utilizo el iterable para definir la cantidad
#de repeticiones entonces no es necesaria la variable

for _ in miLista:
    print("ciclo")
    
    
#si no tengo un iterable puedo usar la funcion
#range() para generar una secuancia de numeros

for x in range(10):
    print(x)
    
#Taller crear un programa que pida un numero al usuario y:
#1, imprima los numeros impares entre -numero y numero
#2. imprima los numeros primos entre o y numero*100
# El programa deb garantizar que el usuario ingrese un numero >0

# entregar antes de las 4 en el repositorio remoto 