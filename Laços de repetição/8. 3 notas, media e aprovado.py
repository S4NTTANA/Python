import os 

os.system ("cls || clear")

soma = 0

for i in range (3):
    nota = int(input(f"Informe a {i+1}ª nota: "))
    soma += nota

media = soma / 3

print (f"Média: {media}")


if (media >= 7): 
    print ("Aprovado!")
if (media < 4):
    print ("Reprovado!")

