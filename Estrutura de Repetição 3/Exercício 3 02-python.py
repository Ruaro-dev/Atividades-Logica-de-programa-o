sexo = 0
homem = 0
mulher = 0
for contador in range(56):
    nome = input("Digite seu nome: ")
    sexo = int(input("Digite seu sexo:\n[1] - Masculino\n[2] - Feminino\nDigite aqui: "))
    if sexo == 1:
        homem +=1
    elif sexo == 2:
        mulher +=1
    else:
        print("Opção Invalida")
print("São\n", homem,"pessoas do sexo masculino\n",mulher,"pessoas do sexo feminino")