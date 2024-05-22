import os 

os.system ("cls || clear")

numeros = []
pares = 0
impares = 0

for i in range (6):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    if i % 2 == 0:
        pares += 1
    else: 
        impares += 1

for i in range (6):
    print (f"Numeros: {numeros[i]}")

print (f"Pares: {pares}")
print (f"Impares: {impares}")
     