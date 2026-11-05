import random
resultado = random.randint(1,50)
for num in range(1,5):
    num = int(input("Escreva o numero: "))
    if num < resultado:
        print("Maior que", num)
    elif num > resultado:
        print("Menor que ",num)
    else: 
        break
print(resultado)
    