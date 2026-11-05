valor = 1
negativos = 0
while valor != 0:
    valor = int(input("Digite qualquer numero:  "))
    if valor <0: 
        negativos += 1
print(negativos,"números negativos")