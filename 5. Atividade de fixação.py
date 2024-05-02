import os

os.system ("cls || clear")

print ("\n=== Solicitando dados ===")
pesoMorangos = float(input("Digite o peso de morangos (em kg): ")
pesoMacas = float(input("Digite o peso de maçãs (em kg): ")

if pesoMorangos < 5:
    precoMorango = 2.50
else : 
    precoMorango = 2.50

if pesoMacas < 5:
    precoMaca = 1.80
else :
    precoMaca = 1.50

pesoTotal = pesoMorangos + pesoMacas
subtotal = (precoMorango * precoMorango) + (precoMaca * pesoMacas)

if pesoTotal > 8 or subtotal > 25:
    desconto = subtotal * 0.10
    
totalPagar = subtotal - desconto

print(f"Peso de maçãs (em kg): {pesoMorangos}")
print(f"Peso de morangos (em kg): {pesoMacaso}")
print(f"Soma dos pesos (em kg): {pesoTotal:.2f})")
print(f"Total a pagar: (totalPagar:.2f)")
print(f"Subtotal: R$ {subtotal:.2f})")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {totalPagar:.2f}")