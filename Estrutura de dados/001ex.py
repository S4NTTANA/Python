import os
from dataclasses import dataclass
os.system ("cls || clear")

# Constante.
QUANTIDADE_ALUNOS = 2

# Classe
@dataclass
class Aluno:
    nomes : str
    idades : int
    alturas : float
    pesos : float

alunos = []


# Solicitando dados para o usuário.
for i in range (QUANTIDADE_ALUNOS):
    nome = input("\nDigite seu nome: ")
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))
    


    aluno = Aluno(nomes = nome, idades = idade, alturas = altura, pesos = peso)
    alunos.append(aluno)

for i in alunos:
    print (f"\nNome: {i.nomes}")
    print (f"Idade: {i.idades}")
    print (f"Altura: {i.alturas}m")
    print (f"Peso: {i.pesos} kg")

#for i in range (len(nomes))