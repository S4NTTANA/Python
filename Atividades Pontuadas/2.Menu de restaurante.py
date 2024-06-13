import os
import time 

def cardapio():
    os.system ("cls || clear")

    print ("              ==== == ======")
    print ("              Menu de Opções")
    print ("              ==== == ======")

    print ("""    |1 - Picanha            R$ 25,00|
    |2 - Lasanha            R$ 20,00|
    |3 - Strogonoff         R$ 18,00|
    |4 - Bife acebolado     R$ 15,00|
    |5 - Pão com ovo        R$ 5,00 |
    |6 - Frango frito       R$ 20,00|
    |7 - Ensopado de carne  R$ 18,00|""")
    
prato = ""
pedidos = []
soma = 0
while True: 
    
    cardapio()
    
    print ("\nPara finalizar o pedido digite 0")
    opcao = int(input("Informe o código do pedido: "))
    
  
    match(opcao):
        case 1:
            resultado = "1 - Picanha - R$ 25,00"
            print ("\nPrato 1 - Picanha")
            print ("Valor - R$ 25,00")
            pedidos.append(resultado)
            soma += 25
        case 2:
            resultado = "2 - Lasanha - R$ 20,00"
            print ("\nPrato 2 - Lasanha")
            print ("Valor - R$ 20,00")
            pedidos.append(resultado) 
            soma += 20
        case 3:
            resultado = "3 - Strogonoff - R$ 18,00"
            print ("\nPrato 3 - Strogonoff")
            print ("valor - R$ 18,00")
            pedidos.append(resultado)
            soma += 18
        case 4:
            resultado = "4 - Bife acebolado"
            print ("\nPrato 4 - Bife acebolado")
            print ("Valor - R$ 15,00")
            pedidos.append(resultado)
            soma += 15
        case 5:
            resutlado = "5 - Pão com Ovo - R$ 5,00"
            print ("\nPrato 5 - Pão com Ovo")
            print ("Valor - R$ 5,00")
            pedidos.append(resultado)
            soma += 5
        case 6:
            resultado = "6 - Frango frito - R$ 20,00"
            print ("\nPrato 6 - Frango frito")
            print ("Valor - R$ 20,00")
            pedidos.append(resultado)
            soma += 20
        case 7:
            resultado = "7 - Ensopado de carne - R$ 18,00"
            print ("\nPrato 7 - Ensopado de carne")
            print ("Valor - R$ 18,00")
            pedidos.append(resultado)
            soma += 18
        case 0:
            print ("Pedido realizado!")
            break
        case _:
            print ("Opção inváldia, tente novamente")
            time.sleep(2)
            os.system("clear")
            
    
    pedido = input("\nDeseja inserir mais um pedido ? s/n: ")
    pedido.upper()    
    if pedido != 's':
        break
            
print ("\n==== == =========")
print ("Modo de Pagamento")
print ("==== == =========")
print ("\n1   |  À vista (10% de desconto)         ")
print ("2   |  Cartão de Crédito (10% de acréscimo)")

pagamento = int(input("\nInforme o código do modo de pagamento: "))

match (pagamento):
    case 1:
        pagamento = "À vista"
        desconto = 0.10
        descontado = soma * desconto
        precoTotal = soma - descontado
        
        print (f"\nPedido: {pedidos}")
        print (f"Forma de pagamento: {pagamento}")
        print (f"Valor do pedido: R$ {soma:.2f}")
        print (f"Valor do desconto: R$ {descontado:.2f}")
        print (f"Valor total do pedido: R$ {precoTotal:.2f}")
    case 2:
        pagamento = "Cartão de crédito"
        inflacao = soma * 0.10
        precoTotal = inflacao + soma
        
        print (f"\nPedido: {pedidos}")
        print (f"Forma de pagamento: {pagamento}")
        print (f"Valor do pedido: R$ {soma:.2f}")
        print (f"Valor da taxa: R$ {inflacao:.2f}")
        print (f"Valor total do pedido: R$ {precoTotal:.2f}")