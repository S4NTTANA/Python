import os 
os.system ("cls || clear")

def calculando_media(notas):
    resultado_media = soma / NOTAS
    return resultado_media
    
def verificando_situacao(media):
    resultado_situacao = "Aprovado!"
    return resultado_situacao if media >= 7 else "Reprovado!"
    
def mostrando_resultado(notas):
    media = calculando_media(notas)
    print (f"Media: {media}")
    print (f"Situação: {verificando_situacao(media)}")
    
    
NOTAS = 3

media = 0
soma = 0

for i in range (NOTAS):
    notas = float(input(f"Informe a {i+1}ª nota: "))
    soma += notas
    

mostrando_resultado(notas)