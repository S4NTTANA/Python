import os

os.system ("cls || clear")

print("=== Solicitando dados ===")
nome = str(input("Informe seu nome: "))
sexo = str(input("Informeo seu genêro (M ou F): "))
estadoCivil = str(input("Informe o seu estado civil: "))

sexo = sexo.lower()
estadoCivil = estadoCivil.lower()

if sexo == "F" and estadoCivil == "Casada":
    tempoCasada = str(input("Informe o tempo de casada: "))

print("\n") 
print("=== Exibindo dados ===") 
print("Nome: {nome}") 
print("Sexo: {sexo}") 
print("Estado civil: {estadoCivil}") 
print("Tempo de casada: {tempoCasada}") 