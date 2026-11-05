numCanal = 0
numP4 = 0
numP5 = 0
numP7 = 0
numP12 = 0
total = 0

while True:
    
    numCanal = int(input("Digite o número do canal: "))
    
    if numCanal == 4:
        numP4 += int(input("Digite o numero de pessoas assistindo: "))
    elif numCanal == 5:
        numP5 += int(input("Digite o numero de pessoas assistindo: "))
    elif numCanal == 7:
        numP7 += int(input("Digite o numero de pessoas assistindo: "))
    elif numCanal == 12:
        numP12 += int(input("Digite o numero de pessoas assistindo: "))
    elif numCanal == 0:
        break
    else:
        print("Tv desligada")

    total = numP4 + numP5 + numP7 + numP12
    
print("A porcentagem de audiencia no canal 4 é ", (numP4*100)/total,"%")
print("A porcentagem de audiencia no canal 5 é ", (numP5*100)/total,"%")
print("A porcentagem de audiencia no canal 7 é ", (numP7*100)/total,"%")
print("A porcentagem de audiencia no canal 12 é ", (numP12*100)/total,"%")