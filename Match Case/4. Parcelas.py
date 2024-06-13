import os

os.system ("cls || clear")

valor = int(input("Informe o valor do produto: "))

while True:

    print ("\n=== Formas de pagamento ===")
    print ("1 - Pagamento à vista")
    print ("2 - Pagamento à prazo")

    formaPagamento = int(input("\nInforme o modo de pagamento: "))


    match (formaPagamento):
        case 1:
            print ("Pagamento à vista")
            desconto = valor * 0.10
            valorTotal = valor - desconto
            print (f"\nValor do produto: {valor}")
            print (f"Forma de pagamento: À vista")
            print (f"Valor do desconto: {desconto}")
            print (f"Total a pagar: {valorTotal}")
            break
        case 2:
            print ("Pagamento à prazo")
            parcelas = int(input("\nInforme a quantidade de parcelas: "))
            valorParcela = valor / parcelas
            print (f"\nValor do produto: {valor}")
            print (f"Forma de pagamento: À prazo")
            print (f"Quantidade de parcelas: {parcelas}")
            print (f"Valor por parcela: {valorParcela}")
            print (f"Total à prazo: {valor}")
            break



