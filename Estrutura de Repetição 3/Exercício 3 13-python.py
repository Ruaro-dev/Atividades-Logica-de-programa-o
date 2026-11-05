paisA = int(input("Digite a população do país A: "))
paisB = int(input("Digite a população do país B: "))
ano = 0

while paisA < paisB:


    paisA += (paisA*0.03)
    paisB += (paisB*0.015)
    ano += 1

    if ano %5 == 0:
        paisA = paisA * 0.93
        paisB = paisB * 0.93

print(ano,"Anos")