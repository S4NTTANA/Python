"""
Descrição das variáveis:
  - quantidade_pares: Quantidade de números pares.
  - quantidade_impares: Quantidade de números ímpares.
  - quantidade_positivos: Quantidade de números positivos.
  - quantidade_negativos: Quantidade de números negativos.
  - maior_numero: O maior número.
  - menor_numero: O menor número.
  - media_pares: Média dos números pares.
  - media_impares: Média dos números ímpares.
  - media_geral: Média de todos os números.
  - numeros_invertidos: Os números na ordem inversa.
"""


# Variáveis para armazenar as estatísticas

numeros = []
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = 0
menor_numero = 999
soma_pares = 0
soma_impares = 0
soma_geral = 0
contador = 0
QTD = 5

# Variáveis para armazenar os números

for i in range (5):
    numero = int(input(f"Digite o {i+1}º numero: "))
    numeros.append(numero)
    contador += 1
    soma_geral += numero
    maior_numero = max(maior_numero, numero)
    menor_numero = min(menor_numero, numero)
    
# Processando cada número

    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
        soma_impares += numero
    
    if numero > 0:
        quantidade_positivos += 1
    if numero < 0:
        quantidade_negativos += 1

if quantidade_pares == 0:
    print ("Não foram informados números pares!")
if quantidade_impares == 0:
    print ("Não foram informados números impares!")
    

media_pares = soma_pares / quantidade_pares if quantidade_pares != 0 else 0
media_impares = soma_impares / quantidade_impares if quantidade_impares != 0 else 0
media_geral = soma_geral / QTD


# Calculando as médias

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")

print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Quantidade de números inseridos: {QTD}")
print(f"Maior numero: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares}")
print(f"Média dos números impares: {media_impares}")
print(f"Média geral: {media_geral}")
numeros.reverse()
print(f"Ordem inversa: {numeros}")
