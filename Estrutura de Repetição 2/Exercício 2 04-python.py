jog1 =0
jog2 = 0
ponto = 0
 
while True:
    ponto = int(input("Digite quem fez ponto\n[1] - jogador 1\n[2] - jogador 2\ndigite aqui: "))
    if ponto == 1:
        jog1 += 1
    elif ponto == 2:
        jog2 += 1 
    else:
        break
    print("JOGADOR 1 - ", jog1,"\nJOGADOR 2 - ", jog2)
    if   jog1 > jog2 and jog1>= 21 and jog1 - jog2 >= 2:
        print("Jogador 1 Venceu!")
        break
    elif  jog2 > jog1 and jog2>= 21 and jog2 - jog1 >= 2:
        print("Jogador 2 Venceu")
        break
    
