contador1 = -1
salario = 0
filhos = 0
somaSalario = 0
somaFilho = 0
maiorSal= 0
salario100= -1
while salario >= 0:
    somaSalario += salario
    somaFilho += filhos
    if salario > maiorSal:              
        maiorSal = salario
    if salario<100:
        salario100 += 1
    

    salario = int(input("Digite seu Sálario: "))
    filhos = int(input("Quantos filhos você tem: "))
    contador1+= 1
    
print("A media Salarial é: ",somaSalario/contador1)
print("A media de Filhos é: ",somaFilho/contador1)
print("O maior Sálario é: ",maiorSal)
print("O percentual de pessoas com Salário até R$100,00 é: ",(salario100*100)/contador1)