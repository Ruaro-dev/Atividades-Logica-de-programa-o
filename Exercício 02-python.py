num = int(input("Digite o Número que você deseja calcular: "))
qtd = int(input("Digite a Quantidade de vezes que você deseja calcular esse número: "))
for contador in range (1, qtd +1 ):
    print(+num, "x" , +contador  , "=" , num * contador)