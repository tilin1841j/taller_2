def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Ingresa un número mayor que cero: "))

while numero <= 0:
    numero = int(input("El número debe ser mayor que cero. Ingresa otro número: "))

print("Números impares entre -{} y {}: ".format(numero, numero))
for i in range(-numero, numero + 1):
    if i % 2 != 0:
        print(i, end=" ")

print("\nNúmeros primos entre 0 y {}: ".format(numero * 100))
for i in range(2, numero * 100):
    if es_primo(i):
        print(i, end=" ")
