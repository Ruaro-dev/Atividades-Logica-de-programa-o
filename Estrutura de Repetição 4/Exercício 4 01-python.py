import random

prodCiclo1 = 0
prodCiclo2 = 0
prodCiclo3 = 0
prodCiclo4 = 0
prodCiclo5 = 0
quebrar1 = 0
quebrar2 = 0
quebrar3 = 0
quebrar4 = 0
quebrar5 = 0
metaFeita = 0

metaDiaria = int(input("Digite a meta diaria: "))
maxCiclo = int(input("Digite o numero maximo de peças por ciclo: "))

ciclo = 0
maquinaQuebrou = 0

while True:
    
    if  metaFeita <= metaDiaria and maquinaQuebrou == 0:
        ciclo += 1

        prodCiclo1 = random.randint(1, maxCiclo)
        metaFeita += prodCiclo1

        if prodCiclo1 > (maxCiclo*0.9):
            quebrar1 += 1
        else:
            quebrar1 = quebrar1 - quebrar1

        if quebrar1 > 4:
            maquinaQuebrou += 1

        prodCiclo2 = random.randint(1, maxCiclo)
        metaFeita += prodCiclo2

        if prodCiclo2 > (maxCiclo*0.9):
            quebrar2 += 1
        else:
            quebrar2 = quebrar2 - quebrar2

        if quebrar2 > 4:
            maquinaQuebrou += 1

        prodCiclo3 = random.randint(1, maxCiclo)
        metaFeita += prodCiclo3

        if prodCiclo3 > (maxCiclo*0.9):
            quebrar3 += 1
        else:
            quebrar3 = quebrar3 - quebrar3

        if quebrar3 > 4:
            maquinaQuebrou += 1

        prodCiclo4 = random.randint(1, maxCiclo)
        metaFeita += prodCiclo4

        if prodCiclo4 > (maxCiclo*0.9):
            quebrar4 += 1
        else:
            quebrar4 = quebrar4 - quebrar4

        if quebrar4 > 4:
            maquinaQuebrou += 1

        prodCiclo5 = random.randint(1, maxCiclo)
        metaFeita += prodCiclo5

        if prodCiclo5 > (maxCiclo*0.9):
            quebrar5 += 1
        else:
            quebrar5 = quebrar5 - quebrar5

        if quebrar5 > 4:
            maquinaQuebrou += 1
    else:
        break

print("Produção total foi de: ", metaFeita)

if maquinaQuebrou >0:
    if quebrar1 >4:
        print("Estação 1 Quebrou")
    elif quebrar2 >4:
        print("Estação 2 Quebrou")
    elif quebrar3 >4:
        print("Estação 3 Quebrou")
    elif quebrar4 >4:
        print("Estação 4 Quebrou")
    else:
        print("Estação 5 Quebrou")

print("Durou ", ciclo, " ciclos")