import os

os.system ("cls || clear")

media : float = 0
soma : float = 0

# Criando uma lista / vetor
notas = []

# Solicitando dados ao usuário
for i in range (3): 
    nota = float(input("Digite uma nota: "))
    notas.append(nota) # Armazena na posição disponível do vetor
    soma += nota
    # sum(notas)
    
media = soma / 3


# Exibindo dados
for i in range (3):
    print(f"Nota: {notas[i]}")

print(f"Média: {media}")
