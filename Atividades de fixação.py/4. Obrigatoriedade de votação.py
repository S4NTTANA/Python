"""Elabore um algoritmo usando operações lógicas para informar se
uma pessoa é obrigada a votar.

Considere que a regra é que menores de 18 e maiores que 65 não
são obrigados a votar."""

import os

os.system("cls || clear")

nome = input("Informe seu nome: ")
idade = int (input("Informe sua idade: "))

if idade > 18 and idade < 65:
    print ("Obrigado a votar.")
else:
    print ("Não é obrigado a votar.")
