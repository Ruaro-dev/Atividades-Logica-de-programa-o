contadorAnp = 0
contadorAp = 0
contadorV = 0
contadorHp = 0
contadorL = 0
while True:
    cod = int(input("Digite o código do Produto: "))
    if cod == 1:
        print("Alimento Não-Perecível")
        contadorAnp += 1
    elif cod >1 and cod <5:
        print("Alimento Perecível")
        contadorAp += 1
    elif cod >4 and cod <7:
        print("Vestuario")
        contadorV += 1
    elif cod == 7:
        print("Higiene pessoal")
        contadorHp += 1
    elif cod >7 and cod <16:
        print("Limpesa e Utensílios Domésticos")
        contadorL += 1
    elif cod == 0:
        break
    else:
        print("Numero invalido, digite outro")
print("A quantidade de Alimento Não-Perecível é ",contadorAnp)
print("A quantidade de Alimento Perecível é ",contadorAp)
print("A quantidade de produtos de Vestuario é ",contadorV)
print("A quantidade de produtos de Higiene pessoal é ",contadorHp)
print("A quantidade de produtos de Limpeza e Utensílios Domésticos é ",contadorL)