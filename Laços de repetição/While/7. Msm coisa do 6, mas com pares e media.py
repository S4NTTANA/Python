import os

os.system ("cls || clear")

soma = 0
somaPares: int = 0
quantidadeNumeros = 0
pares = 0
quantidadePares = 0

while True : 
    numero = int(input(f"Informe um número: "))
    if numero == 0:
        break
    quantidadeNumeros += 1
    soma += numero

    if numero % 2 == 0:
        somaPares += numero
        pares += 1
        quantidadePares += 1

media = soma / quantidadeNumeros
mediaPares = somaPares / quantidadePares

print (f"\nQuantidade de números inseridos: {quantidadeNumeros}")
print (f"Média pares: {mediaPares}")
print (f"Media geral: {media}")


