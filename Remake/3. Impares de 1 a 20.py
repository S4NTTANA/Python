import os
os.system ("cls || clear")

def contando (condicao):
    for i in range (1, 21):
        if i % 2 == 1:
            print (f"Contando números ímpares de 1 a 20: {i}")
       
condicao = input("Informe se deseja rodar o programa (s/n): ")
if condicao == 's':
    contador = contando (condicao)
else:
    print ("Fim do programa!")