import os
from dataclasses import dataclass
os.system ("cls || clear")

BICHOS = 2

# Classe
@dataclass
class Dados:
    def __init__(self, nome, idade, raca, porte, alimentacao):
        self.nomes = nome
        self.idades = idade
        self.racas = raca
        self.portes = porte
        self.alimentacoes = alimentacao
bichos = []


# Solicitando dados para o usuário.
for i in range (BICHOS):
    nome = input(f"\nDigite o nome do {i+1}º animal: "),
    idade = input(f"Digite a idade de {nome}: "),
    raca = int(input("Digite a raça de {nome}: ")),
    porte = float(input(f"Informe o porte de {nome}: "))
    alimentacao = float(input(f"Digite a alimentação de {nome}: "))

    dados = Dados(nomes = nome, idades = idade, racas = raca, portes = porte, alimentacoes = alimentacao)

for i in bichos:
    print (f"\nNome: {i.nomes}")
    print (f"Idade de {nome}: {i.idade}")
    print (f"Raça de {nome}: {i.racas}")
    print (f"Porte de {nome}: {i.portes}")
    print (f"Alimentação de {nome}: {i.alimentacoes}")