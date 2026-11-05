num = 0
numP = 0
numN = 0
while True:
    num = int(input("Digite um Número: "))
    if num > 0:
        numP += num
    elif num < 0:
        numN += num
    else:
        break
    if num %2 == 0:
        print(num, "Par")
    else:
        print(num, "Impar")
print ("A soma dos positivos é: ", numP)
print("A soma dos negativos é: ",numN)
print("A soma das parciais é: ",numP + numN)