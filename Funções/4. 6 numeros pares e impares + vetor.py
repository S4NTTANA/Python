import os 

os.system ("cls || clear")

def logosenai():
    os.system ("cls || clear")
    print ("=== ===== ===")
    print ("=== SENAI ===")
    print ("=== ===== ===")     

def verificaP(number):
    pares = 0
    for numero in number:
        if numero % 2 == 0:
            pares += 1
    return pares

def verificaI(number):
    impares = 0
    for numero in number:
        if numero % 2 != 0:
            impares += 1
    return impares
lista = []

logosenai()
for i in range (6):
    numero = int(input(f"Informe o {i+1}º numero: "))
    lista.append(numero)

quantiP = verificaP(lista)
quantiI = verificaI(lista)

logosenai()

print (f"Quantidade de pares: {quantiP}")
print (f"Quantidade de impares: {quantiI}")
