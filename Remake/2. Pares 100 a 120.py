import os
os.system ("cls || clear")

def contando (condicao):
        for i in range (100,121):
            if i % 2 == 0:
                print (f"Contando pares de 100 a 120: {i}")
        
condicao = input("Informe se deseja roda o programa (s/n): ")
if condicao == 's':
    contador = contando (condicao)
else:
    print ("Fim do programa!")

