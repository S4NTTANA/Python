import os

os.system ("cls || clear")

contadorNotas = 0
soma = 0

while True:
    nota = float(input(f"Digite a nota: "))
    resposta = input(f"Deseja inserir mais uma nota ?")

    resposta = resposta.upper()

    if resposta != "N":
        soma += nota
        contadorNotas += 1
    else:
        break

media = soma / contadorNotas

print (f"Média: {media}")


