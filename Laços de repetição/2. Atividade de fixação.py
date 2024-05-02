import os

os.system ("cls || clear")

print("\n === Solicitando dados ===")
numero = int(input("Digite um número para tabuada: "))

for i in range (1,11):
    print(f"{numero} x {i} = {numero * i}")