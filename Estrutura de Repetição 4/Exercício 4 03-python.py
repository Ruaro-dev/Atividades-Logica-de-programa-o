desgaste = 0
ciclo = 0
while desgaste <500:
    ciclo += 1

    if ciclo >70:
        desgaste += 10
    else:
        desgaste += 7
print("Durou ",ciclo,"ciclos")
print("\nE o destaste final foi de: ", desgaste)