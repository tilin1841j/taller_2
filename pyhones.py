# comentario de una linea 
# todo lo que va despues es ignorado por el
# interpetre de python 

# variables: Espacio de memoria, con nombre, donde guardo valores
# Los nombres de variables deben ser cortos, descriptivos, NO TENER ESPACIOS
# EN BLANCO ni caracteres especiales, no deben empezar por un números

#descriptivo significa que representa la categoria del datos que quiero guardar 
# en python las variables pueden contener cualquier dato de tipo primitivo 
# numeros (enteros, reales), cadenas de caracteres (string). boolenos (true. false)
#caracteres (letras).

variable= 1

variable= 'juventud divino tesoro, te vas para no volver, cuando quiero llorar pero no lo hare'
variable= True

variable= 'a'

variable= 3.1415926535

# para signar un valor a la variable se usa el operador=

#Operadores: Mecanismo para obtener un dato a partir de otros datos.
#los datos que intervienen s llaman operados 
#Aritmeticos : + - * / %

#De comparacion: Retornan true or false. > < >= <= == !=

#Los de logica booleana: OR AND. Retornan true o false de acuerdo a una
#tabla de verdad.los operadores siempre son boolenaos (True or False)

a=True
b=False

print(a and b)

#los operadores booleanos y de comparacion son muy utilizados al
# definir condiciones

#sentencias de control de codigo: En general un programa se ejecuta
# Linea por linea de manera secuancial. Se puede romper esa secuencialidad
# empleado un conjunto de sentencias (expresiones) que permite:
# 1. seleccionar la ejecucion de un bloque de codigo
# 2. Reptir la ejecucion de uin bloque de codigo
# 3. seleccionar entre ejecutar un bloque de codigo u otro bloque de codigo
# De esa manera podemos "romper" la secuencialidad
# Principos de paradigma de programacion estructurado

# sentencia if. si se cumple una condicion (se evalua como true)
# se ejecuta un bloque de codigo

print("linea 1")
print("linea 2")
if 5>8 or 3<7:
    print("Esto se muetra si la condicion es verdadera")
    
else:
    print("Esto se muetra si la condicion es false")
    
entrada= int (input("cuantos años tiene?"))

if entrada< 18:
    print("Es un menor de edad")
    
else: 
    print("ya no esta disponible para su edad")
    
#taller crear un programa en python que genere un numero aleatroio 
#Entre 2 y 12. si el numero es 7 imprimir gano. si no imprimir perdio 

