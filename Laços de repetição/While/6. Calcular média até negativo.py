import os

os.system ("cls || clear")

soma : int = 0
quantidadeNumeros = 0

while True : 
    numero = int(input(f"Informe um número: "))
    if numero < 0:
        break

    soma += numero
    quantidadeNumeros += 1


media = soma / quantidadeNumeros

print ("fMédia: {media}")

