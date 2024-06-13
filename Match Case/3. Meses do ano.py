import os 

os.system ("cls || clear")

print ("===== == ===")
print ("Meses do ano")
print ("===== == ===")

print ("1 - Janeiro")
print ("2 - Fevereiro")
print ("3 - Março")
print ("4 - Abril")
print ("5 - Maio")
print ("6 - Junho")
print ("7 - Julho")
print ("8 - Agosto")
print ("9 - Setembro")
print ("10 - Outubro")
print ("11 - Novembro")
print ("12 - Dezembro")

while True:

    MesAno = int(input("\nInforme o número do mês do ano: "))

    match (MesAno):
        case 1:
            print ("Janeiro")
            break 
        case 2:
            print ("Fevereiro") 
            break
        case 3:
            print ("Março") 
            break 
        case 4:
            print ("Abril") 
            break 
        case 5:
            print ("Maio") 
            break
        case 6:
            print ("Junho") 
            break 
        case 7:
            print ("Julho") 
            break 
        case 8:
            print ("Agosto")  
            break 
        case 9:
            print ("Setembro") 
            break 
        case 10:
            print ("Outubro") 
            break 
        case 11:
            print ("Novembro") 
            break 
        case 12:
            print ("Dezembro") 
            break 
