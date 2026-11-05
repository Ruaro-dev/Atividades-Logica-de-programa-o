temperatura = 0.0
tempvalida = 0
maiortemp = 0.0
tempTotal = 0
while temperatura != 999:

    temperatura = float(input("Digite a temperatura: "))

    tempTotal += 1

    if temperatura >=20 and temperatura <=80 and temperatura %5 ==0 and temperatura %10 != 0:
        print(temperatura," é uma temperatura valida")
        tempvalida +=1
        if temperatura > maiortemp:
            maiortemp = temperatura

print("O percentual final das temperaturas validas é de: ",(tempvalida*100)/tempTotal)
print("\nA maior temperatura valida é: ",maiortemp)