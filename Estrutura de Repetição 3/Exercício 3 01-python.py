num = 0
numEntre = 0
for num in range(150):
    num = int(input("Digite um número: "))
    if num >=10 and num <=150:
        numEntre += 1
print(numEntre," Números estão entre 10 e 150")