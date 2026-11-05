avaliacao = 0
idade = 0
qtdTotal = 0
qtdPessimo = 0
qtdBom = 0
qtdExcelente = 0
idadeExelente = 0

while qtdTotal < 35:
    avaliacao = int(input("Digite a avaliação, sendo:\n[1] - Pessimo\n[2] - Regular\n[3] - bom\n[4] - excelente\nDigite aqui: "))
    idade = int(input("Digite sua idade: "))

    if avaliacao == 1:
        qtdTotal += 1
        qtdPessimo +=1
    
    elif avaliacao == 2:
        qtdTotal += 1

    elif avaliacao == 3:
        qtdTotal += 1
        qtdBom += 1

    elif avaliacao == 4:
        qtdTotal += 1
        qtdExcelente += 1
        idadeExelente += idade
    else:
        print("código invalido, digite novamente")

print("A média de idade dos clientes que avaliaram como excelente: ", idadeExelente/qtdExcelente,"anos")
print("\nO total de clientes que avaliaram como péssimo foram: ",qtdPessimo)
print("\nA porcentagem de clientes que avaliaram como bom foi",(qtdBom*100)/qtdTotal,"%")        
