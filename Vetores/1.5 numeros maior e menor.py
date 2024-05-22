import os

os.system ("cls || clear")

numeros = []
maiorN = 0
menorN = 999

for i in range (5):
    numero  = float(input("Digite uma nota: "))
    numeros.append(numero)
    menorN = min (numero, menorN)
    maiorN = max (numero, maiorN)

for i in range (5):
    print (f"Números: {numeros[i]}")

print (f"Maior numero: {maiorN}")
print (f"Menor numero: {menorN}")





