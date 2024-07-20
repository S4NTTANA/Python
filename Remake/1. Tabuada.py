import os
os.system ("cls || clear")

def tabuada(numero):
    for i in range (1, 11):
        print (f"{numero} x {i} = {numero * i}")

numero = int(input("Informe o número a ser calculado na tabuada: "))

tabu = tabuada(numero)