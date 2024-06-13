import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def IMC (peso, altura):
    imc = peso / (altura*altura)
    return imc
    
def resultadoImc (imc):
    if imc < 18.5:
        resultado = "Abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        resultado = "Peso normal"
    elif imc >= 25 and imc < 30:
        resultado = "Sobrepeso"
    elif imc >= 30 and imc < 35:
        resultado = "Obesidade Grau I"
    elif imc >= 35 and imc < 40:
        resultado = "Obesidade Grau II"
    elif imc >= 40:
        resultado = "Obesidade Grau III (Mórbida)"
    return resultado
    
# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []
sobrenomes = []


# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    if nome.lower() == 'sair':
        break
    sobrenome = input("Digite o seu sobrenome: ")
    
    if sobrenome.lower() == 'sair':
        break
    # Verificando se o usuário quer sair
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    sobrenomes.append(sobrenome)
    
    
   # calculo = resultadoImc (calculandoImc) 
    
# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i], sobrenomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")

    calculandoImc = IMC (pesos[i], alturas[i])
    print("Situação com base no IMC: ", resultadoImc(calculandoImc))
    print()