import os

os.system ("cls || clear")

print ("             === ======== ===")
print ("             === Cardápio ===")
print ("             === ======== ===")

print ("""
Código       Prato            valor
       
  1    -     Picanha         R$ 25,00
       
  2    -     Lasanha         R$ 20,00
       
  3    -     Strogonoff      R$ 18,00
       
  4    -    Bife acebolado   R$ 15,00
       
  5    -     Pão com ovo     R$ 5,00
""")

while True: 
    opcao = int(input("Informe a opção: "))

    match (opcao):
        case 1:
            print("Prato - Picanha")
            print("Valor - R$ 25,00")
             
        case 2:
            print("Prato - Lasanha")
            print("Valor - R$ 20,00")
            
        case 3:
            print("Prato - Strogonoff")
            print("Valor - R$ 18,00")
            
        case 4:
            print("Prato - Bife Acebolado")
            print("Valor - R$ 15,00")
            
        case 5:
            print("Prato - Pão com Ovo")
            print("Valor - R$ 5,00")
            
        case 0:
            print ("Pedido realizado")
            break