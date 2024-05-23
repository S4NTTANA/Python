import os

def logosenai():
    os.system ("cls || clear")
    print ("=== ===== ===")
    print ("=== SENAI ===")
    print ("=== ===== ===")

logosenai()
nome = input("Digite o seu nome: ")

logosenai()
idade = int(input("Digite o sua idade: "))

logosenai()
peso = float(input("Digite o seu peso: "))

logosenai()
print (f"Nome: {nome}")
print (f"Idade: {idade}")
print (f"Peso: {peso: .2f}")