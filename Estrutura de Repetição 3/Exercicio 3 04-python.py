codigo = 0
valor = 0
valorPrest = 0
totalAvista = 0
totalAprazo = 0

for i in range(15):
    valor = float(input("Digite o valor da compra: "))
    codigo = int(input("Digite se deseja pagar à vista ou à prazo, sendo:\n[1] - À vista\n[2] - À prazo\nDigite aqui: "))
    if codigo == 1:
        totalAvista += valor
    elif codigo == 2:
        totalAprazo += valor
    else:
        print("valor invalido, digite novamente")

print("O valor total das compras á vista é: R$", totalAvista)
print("O valor total das compras á prazo é: R$", totalAprazo)
print("O valor total das compras é: R$", totalAvista + totalAprazo)
print("O valor total da primeira prestação das compras á prazo é: R$", totalAprazo/3)