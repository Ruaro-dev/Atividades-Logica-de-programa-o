valorJuros = 0.0
valorParcela = 0.0
valorDivida = float(input("Digite o valor da divida: "))
qtdParcelas = int(input("Digite quantas parcelas deseja: "))

if qtdParcelas == 1:
    valorJuros = 0
    valorParcela = 0
elif qtdParcelas == 3:
    valorJuros = valorDivida * 0.1
    valorDivida = valorDivida + valorJuros
    valorParcela = valorDivida/qtdParcelas
elif qtdParcelas == 6:
    valorJuros = valorDivida * 0.15
    valorDivida = valorDivida + valorJuros
    valorParcela = valorDivida/qtdParcelas
elif qtdParcelas == 9:
    valorJuros = valorDivida * 0.2
    valorDivida = valorDivida + valorJuros
    valorParcela = valorDivida/qtdParcelas
elif qtdParcelas == 12:
    valorJuros = valorDivida * 0.25
    valorDivida = valorDivida + valorJuros
    valorParcela = valorDivida/qtdParcelas

print ("Valor da Dívida: R$",valorDivida)
print ("\nValor dos Juros: R$",valorJuros)
print ("\nA quantidade de parcelas é: ",qtdParcelas)
print ("\nValor da parcela: R$",valorParcela)