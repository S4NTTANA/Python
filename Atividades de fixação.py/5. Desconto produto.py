"""Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida
e o preço unitário.

Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto
e o total a pagar (total a pagar = total - Gesconto), sabendo-se que:

- Se quantidade <= 5 o desconto será de 2%
- Se quantidade > 5 e quantidade <= 10 o desconto será de 3%
- Se quantidade > 10 o desconto será de 5%."""

import os
os.system("cls || clear")

produto = input("Informe o nome do produto: ")
quantidade = int(input("Informe a quantidade: "))
preco = float(input("Informe o preço por unidade: "))


if quantidade <= 5:
    desconto = 0.02
elif quantidade > 5 and quantidade <= 10:
    desconto =  0.03
if quantidade > 10:
    desconto = 0.05

    total = quantidade * preco
    totalD = total -(total * desconto)

    print ("total a pagar: {}", totalD)