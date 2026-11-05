cod = 0
qtd = 0
valorTotal = 0.0
cQ = 0.0
bauruS = 0.0
bauruOvo = 0.0
hamb = 0.0
cheese = 0.0

print("CARDAPIO")
print("\n\n Cachorro Quente - Codigo [100] - Valor: 1,20")
print("\n Bauru simples - Codigo [101] - Valor: 1,30")
print("\n Bauru com ovo - Codigo [102] - Valor: 1,50")
print("\n Hamburguer - Codigo [103] - Valor: 1,20")
print("\n Cheeseburguer - Codigo [104] - Valor: 1,30")
print("\n Refrigerante - Codigo [105] - Valor: 1,00")

while True:
    cod = int(input("Digite o Codigo do pedido: "))
    qtd = int(input("Digite a quantidade que deseja: "))

    if cod == 100:
        nomeLanche = "Cachorro Quente"
        cQ = 1.2 * qtd
        valorTotal += cQ
    elif cod == 101:
        nomeLanche = "Bauru simples"
        bauruS = 1.3 * qtd
        valorTotal += bauruS
    elif cod == 102:
        nomeLanche = "Bauru com ovo"
        bauruOvo = 1.5 * qtd
        valorTotal += bauruOvo
    elif cod == 103:
        nomeLanche = "Hamburguer"
        hamb = 1.2 * qtd
        valorTotal += hamb
    elif cod == 104:
        nomeLanche = "Cheeseburguer"
        cheese = 1.3 * qtd
        valorTotal += cheese
    elif cod == 105:
        nomeLanche = "Refrigerante"
        refri = 1.2 * qtd
        valorTotal += refri
    elif cod == 0:
        break
    else:
        print("Digite o codigo corretamente")

    print("--- ",nomeLanche," ---")
    print("\n",qtd," unidades")

    if cod == 100:
        print("\nR$",cQ)
    elif cod == 101:
        print("\nR$",bauruS)
    elif cod == 102:
        print("\nR$",bauruOvo)
    elif cod == 103:
        print("\nR$",hamb)
    elif cod == 104:
        print("\nR$",cheese)
    elif cod == 105:
        print("\nR$",refri)

print("O valor final ficou: R$", valorTotal)