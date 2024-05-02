"""3. Elabore um algoritmo para ler o nome de um aluno, sua idade e as
três notas. Calcular a média do aluno.

Caso a média do aluno seja menor que 7, o aluno está reprovado.

Mostrar: nome, idade, média e se está aprovado ou reprovado."""

import os 

os.system ("cls || clear")

nome = str
idade = int
N1 = float
N2 = float
N3 = float

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
N1 = float (input("Digite sua primeira nota: "))
N2 = float(input("Digite sua segunda nota: "))
N3 = float(input("Digite sua terceira nota: "))

media = (N1 + N2 + N3) / 3

print (f"\nNome: {nome}")
print (f"Idade: {idade}")
print (f"Primeira nota: {N1}")
print (f"Segunda nota: {N2}")
print (f"Terceira nota: {N3}")
print (f"Media: {media}")

if media < 7:
    print("Reprovado.")
else:
    print("Aprovado.")




