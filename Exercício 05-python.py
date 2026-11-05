num = 1
numPares = 0
SomaNumPares = 0
while num != 0:
    num = int(input("Digite seu numero: "))
    if num ==0:
            break
    if num % 2 == 0:
        numPares+=1
        SomaNumPares += num
print("Media ",(SomaNumPares / numPares))