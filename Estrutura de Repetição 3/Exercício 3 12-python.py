qtdmultiplos3 = 0
qtdSomaPares = 0
num = 0
for i in range(50):
    num = int(input("Digite um número: "))

    if num %3 == 0:
        qtdmultiplos3 += 1
    if num %2 ==0:
        qtdSomaPares += num
    
print(qtdmultiplos3, "Números são multiplos de 3")
print("\n",qtdSomaPares, "É a soma dos números pares")