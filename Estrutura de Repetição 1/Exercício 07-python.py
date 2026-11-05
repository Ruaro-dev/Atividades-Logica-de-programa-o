num = 0
somanum = 0
mediaP = 0
contador = 0
while True:
    num = float(input("Digite seu Número: "))
    if num < 0:
        break
    if num > 0:
        contador += 1
    somanum += num
    mediaP= (somanum/contador)
print("A média é", mediaP)
    
    