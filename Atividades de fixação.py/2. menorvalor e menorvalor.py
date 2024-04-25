import os
os.system ("cls || clear")

N1 = int
N2 = int
soma = int
media = float
produto = int
menorV = int
maiorV = int


N1 = int (input("Digite o primeiro número: "))
N2 = int (input("Digite o segundo número: "))

soma = N1 + N2
media = (N1 + N2) / 2
produto = N1 * N2

if N1 < N2:
    menorV = N1
    maiorV = N2
else:
    maiorV = N1
    menorV = N2

print (f"\nPrimeiro número: {N1}")
print (f"Segundo número: {N2}")
print (f"Média: {media}")
print (f"Soma: {soma}")
print (f"Produto: {produto}")
print (f"Menor valor: {menorV}")
print (f"Maior valor: {maiorV}")