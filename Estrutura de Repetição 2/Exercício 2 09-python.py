bonus = 0
compra = 0
for nome in range(150):
    nome = input("Digite o nome do cliente: ")
    compra = float(input("Digite o valor das compras do cliente: "))
    if compra < 500000:
        bonus = compra * 0.10
    else:
        bonus = compra * 0.15
    print("Cliente: ", nome)
    print("Bonus a receber: R$",bonus)  