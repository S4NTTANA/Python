import os
os.system ("cls || clear")
def logosenai():
    os.system ("cls || clear")
    print ("=== SENAI ===")
    
def calculoInss(salario):
    if salario < 1100.01:
        descontoInss = salario * 0.075
    elif salario < 2203.49:
        descontoInss = salario * 0.09
    elif salario < 3305.23:
        descontoInss = salario * 0.12
    elif salario < 6433.58:
        descontoInss = salario * 0.14
    else:
        descontoInss = 854.36
    return descontoInss

def calculoIrff(salario):
    deducaoDependente = quantidadeDependente * 189.59
    
    if salario < 2259.21: 
        descontoIrff = 0
    elif salario < 2826.66:
        descontoIrff = salario * 0.075
    elif salario < 3751.06:
        descontoIrff = salario * 0.15
    elif salario < 4664.69:
        descontoIrff = salario * 0.225
    else:
        descontoIrff = salario * 0.275
    
    descontoIrff = descontoIrff + deducaoDependente
 
    return descontoIrff
        
def calculoTransporte(salario):
    descontoTransporte = salario * 0.06
    return descontoTransporte if  valeTrans.lower() == 's' else 0
    
def calculoRefeicao(valeRef):
    descontoRefeicao = valeRef * 0.2
    return descontoRefeicao

def calculoSaude(quantidadeDependente):
    descontoSaude = 150 + (150 * quantidadeDependente)
    return descontoSaude
    
class Dados:
    def __init__(self, matricula, senha, salario, valeRef, valeTrans,calcularInss, calcularIrff, calcularTransporte, calcularSaude, calcularRefeicao, descontoTotal):
        self.matricula = matricula
        self.senha = senha
        self.salario = salario
        self.valeRef = valeRef
        self.valeTrans = valeTrans
        self.calcularInss = calcularInss
        self.calcularIrff = calcularIrff
        self.calcularTransporte = calcularTransporte
        self.calcularSaude = calcularSaude
        self.calcularRefeicao = calcularRefeicao
        self.descontoTotal = descontoTotal

dados = []

matricula = input("\nInforme a sua matrícula: ")
senha = input("Informe a sua senha: ")
salario = float(input("informe o seu salario: "))
valeTrans = str(input("Deseja receber vale transporte (s/n): "))

quantidadeDependente = int(input("Informe a quantidade de dependentes: "))

    
valeRef = float(input("Informe o valor do vale refeição: "))

calcularInss = calculoInss(salario)
calcularIrff = calculoIrff(salario)
calcularTransporte = calculoTransporte(salario)
calcularRefeicao = calculoRefeicao(valeRef)
calcularSaude = calculoSaude(quantidadeDependente)
    
descontoTotal = calcularInss + calcularIrff + calcularTransporte + calcularSaude + calcularRefeicao
salarioLiquido = salario - descontoTotal
    
dados.append(Dados(matricula, senha, salario, valeTrans, valeRef, calcularInss, calcularIrff, calcularTransporte, calcularSaude, calcularRefeicao, descontoTotal))
    
for i, coletados in enumerate(dados): 
    logosenai()
    print ("===== == =========")
    print ("Folha de Pagamento")
    print ("===== == =========")
    print ("\nMatrícula: ", coletados.matricula)
    print ("Senha: ", coletados.senha)
    print (f"Salário Bruto: R$", round(coletados.salario,2))
    print (f"INSS (Instituto Nacional do Seguro Social) : R$ {round(calcularInss,2)}")
    print (f"IRRF (Imposto de Renda Retido na Fonte) : R$ {round(calcularIrff,2)}")
    print (f"Vale refeição: R$", round(coletados.calcularRefeicao,2))
    print (f"Vale transporte: R$", round(coletados.calcularTransporte,2))
    print (f"quantidadeDependente de dependentes: {quantidadeDependente}")
    print (f"Plano de saúde: R$ {round(calcularSaude,2)}")
    print (f"Desconto Total:  R$ {coletados.descontoTotal:.2f}")
    print (f"Salario Líquido: R$", round(salarioLiquido,2))
        