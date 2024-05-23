import os 

def logosenai():
    os.system ("cls || clear")
    print ("=== ===== ===")
    print ("=== SENAI ===")
    print ("=== ===== ===")

def somar(A,B):
    resultado = A + B
    return resultado
def sub(A,B):
    resultado = A - B
    return resultado
def dividir(A,B):
    resultado = A / B
    return resultado
def mult(A,B):
    resultado = A * B
    return resultado

logosenai()
premero = int(input("Digite o primeiro numero: "))

logosenai()
sergundo = int(input("Digite o segundo numero: "))

soma = somar (premero, sergundo)
subtracao = sub (premero, sergundo )
multiplicacao = mult (premero, sergundo )
divisao = dividir (premero, sergundo )

logosenai ()
print(f"soma: {soma}")
print(f"subtracao: {subtracao}")
print(f"multiplicacao: {multiplicacao}")
print(f"divisao: {divisao}")

    
