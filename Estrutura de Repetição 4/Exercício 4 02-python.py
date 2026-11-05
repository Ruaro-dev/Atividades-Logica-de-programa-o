temperatura = float(input("Informe a temperatura: "))
ciclo = 0

while temperatura <1000:
    ciclo +=1

    if temperatura <800:
        temperatura = temperatura + 50
    if temperatura <1000:
        temperatura = temperatura + 20

print("A temperatura final foi: ",temperatura,"°C")
print("\nE foram necessadrios ",ciclo," ciclos")