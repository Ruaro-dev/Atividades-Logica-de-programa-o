avaliacao = 0
idade = 0
totalIdade = 0
qtdPessoas1 = 0
qtdPessoas2 = 0
qtdPessoas3 = 0
totalPessoas = 0
percentagemBom = 0
for i in range (15):
    idade = int(input("Insira sua idade: "))
    avaliacao = int(input("Avalie o filme, sendo:\n[3] - Ótimo\n[2] - Bom\n[1] - Regular\nDigite aqui: "))
    if avaliacao == 3:
        totalIdade += idade
        qtdPessoas1 +=1
    elif avaliacao == 2:
        qtdPessoas2 += 1
    elif avaliacao == 1:
        qtdPessoas3 +=1
    totalPessoas = qtdPessoas1 + qtdPessoas2 + qtdPessoas3
    percentagemBom = (qtdPessoas2*100)/totalPessoas
print("A média das pessoas que responderam ótimo é: ",totalIdade/qtdPessoas1 ,"anos")
print("\nA quantidade de pessoas que responderam regular é: ",qtdPessoas3)
print("\nA percentagem das pessoas que responderam bom é: ",percentagemBom,"%")