import os 

os.system ("cls || clear")

def logosenai():
    os.system ("cls || clear")
    print ("=== ===== ===")
    print ("=== SENAI ===")
    print ("=== ===== ===")

def inflaction(valor):
    if valor < 100: 
        inflaction = (valor * 0.1) + valor

    if valor >= 100:
        inflaction = (valor * 0.2) + valor
    return inflaction

logosenai()
valor = float(input("Informe o valor do produto: "))


inflection = inflaction(valor)

logosenai()
print (f"Valor inflacionado: {inflection}")
