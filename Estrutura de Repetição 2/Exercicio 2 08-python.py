valorF = 0
pr = 0
valorP = 0
valorC = int(input("Escreva o Valor do carro: "))
pag = int(input("Escreva a forma de pagamento 1-A vista\n2-Parcelado"))

if pag == 1:
    valorF = valorC * 0.8
    print(valorF)
elif pag == 2:
    pr = int(input("Quantas parcelas?\n[1] - 6\n[2] - 12\n[3] - 18\n[4] - 24\n[5] - 30\n[6] - 36\n[7] - 42\n[8] - 48\n[9] - 54\n[10] - 60\n Digite aqui: "))
    if pr == 1:
        valorP = (valorC / 6)+(valorC/6)*0.03
        valorF = valorP * 6
        print("R$", valorF, "a quantidade de parcelas é 6, o valor da parcela é R$",valorP)
    elif pr == 2:
        valorP = (valorC / 12)+(valorC/12)*0.06
        valorF = valorP * 12
        print("R$", valorF, "a quantidade de parcelas é 12, o valor da parcela é R$",valorP,)
    elif pr == 3:
        valorP = (valorC / 18)+(valorC/18)*0.09
        valorF = valorP * 18
        print("R$", valorF, "a quantidade de parcelas é 18, o valor da parcela é R$",valorP,)
    elif pr == 4:
        valorP = (valorC / 24)+(valorC/24)*0.12
        valorF = valorP * 24
        print("R$", valorF, "a quantidade de parcelas é 24, o valor da parcela é R$",valorP,)
    elif pr == 5:
        valorP = (valorC / 30)+(valorC/30)*0.15
        valorF = valorP * 30
        print("R$", valorF, "a quantidade de parcelas é 30, o valor da parcela é R$",valorP,)
    elif pr == 6:
        valorP = (valorC / 36)+(valorC/36)*0.18
        valorF = valorP * 36
        print("R$", valorF, "a quantidade de parcelas é 36, o valor da parcela é R$",valorP,)
    elif pr == 7:
        valorP = (valorC / 42)+(valorC/42)*0.21
        valorF = valorP * 42
        print("R$", valorF, "a quantidade de parcelas é 42, o valor da parcela é R$",valorP,)
    elif pr == 8:
        valorP = (valorC / 48)+(valorC/48)*0.24
        valorF = valorP * 48
        print("R$", valorF, "a quantidade de parcelas é 48, o valor da parcela é R$",valorP,)
    elif pr == 9:
        valorP = (valorC / 54)+(valorC/54)*0.27
        valorF = valorP * 54
        print("R$", valorF, "a quantidade de parcelas é 54, o valor da parcela é R$",valorP,)
    elif pr == 10:
        valorP = (valorC / 60)+(valorC/60)*0.30
        valorF = valorP * 60
        print("R$", valorF, "a quantidade de parcelas é 60, o valor da parcela é R$",valorP,)