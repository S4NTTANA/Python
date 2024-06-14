import os
import math
from dataclasses import dataclass

# Declarando funções
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def calcular_imc(peso, altura):
    return peso / math.pow(altura, 2)

def resultado_imc(imc):
    if imc < 18.5:
        resultado = "Muito magro"
    elif imc < 25:
        resultado = "Peso normal"
    elif imc < 30:
        resultado = "Sobrepeso"
    elif imc < 35:
        resultado = "Obesidade grau I"
    elif imc < 40:
        resultado = "Obesidade grau II"
    else:
        resultado = "Obesidade grau III (mórbida)"

    return resultado

# Classes
@dataclass
class Dados:
    def __init__(self, nomes, sobrenomes, idades, alturas, pesos):
        self.nomes = nomes
        self.sobrenomes = sobrenomes
        self.idades = idades
        self.alturas = alturas
        self.pesos = pesos

# Declarando vetores
dados = []
imcs = []
resultados_imcs = []
nomes_completos = []

# Solicitando dados no laço de repetição
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    if nome.lower() == 'sair':
        break
    
    sobrenome = input("Digite o sobrenome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    dados.append(Dados(nome, sobrenome, idade, altura, peso))
    #dados = Dados(nome, sobrenome, idade, altura, peso)

    nomes_completos.append(nome + " " + sobrenome)
    imc = calcular_imc(peso, altura)

    imcs.append(imc)
    resultados_imcs.append(resultado_imc(imc))

# Mostrando dados solicitados
logoSenai()
print("\nDados dos usuários: \n")
for i, coletados in enumerate(dados):
    print(f"Usuário {i+1}:")
    print("Nome:", coletados.nomes)
    print("Sobrenome:", coletados.sobrenomes)
    print("Nome completo:", nomes_completos[i])
    print("Idade:", coletados.idades)
    print("Altura:", coletados.alturas, "m")
    print("Peso:", coletados.pesos, "Kg")
    print("IMC:", round(imcs[i], 2))
    print("Resultado:", resultados_imcs[i])
    print()