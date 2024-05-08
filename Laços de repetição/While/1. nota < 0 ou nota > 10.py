import os

os.system ("cls || clear")

nota = int(input(f"Informe a nota: "))

while (nota < 0 or nota > 10):
    nota = int(input(f"Informe a nota: "))

print (f"Nota: {nota}")