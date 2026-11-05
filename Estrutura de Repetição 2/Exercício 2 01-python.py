maiorAcidentes = -1; tv = 0; tvesc = 0; tvepr = 0; tvers = 0; vA = 0; vP = 0; ta = 0; taPR = 0; taSC = 0; taRS = 0; mediaVEpr = 0; mediaVEsc = 0; mediaVErs = 0; cp = 0; cm = 0; mediaTotal = 0; mediaAsc = 0; menorAcidentes = float('inf')

for i in range(12):
    cdc = int(input("Codigo Cidade: "))              
    if cdc == 11:
        nome_cidade = "Jaraguá do Sul-SC"
    elif cdc == 12:
        nome_cidade = "Joinville-SC"
    elif cdc == 13:
        nome_cidade = "Blumenau-SC"
    elif cdc == 14:
        nome_cidade = "Florianopólis-SC"
    elif cdc == 21:
        nome_cidade = "Porto Alegre-RS"
    elif cdc == 22:
        nome_cidade = "Bento Gonçalves-RS"
    elif cdc == 23:
        nome_cidade = "GARIBALDI-RS"
    elif cdc == 24:
        nome_cidade = "Caxias do Sul-RS"
    elif cdc == 31:
        nome_cidade = "Curitiba-PR"
    elif cdc == 32:
        nome_cidade = "Foz do Iguaçu-PR"
    elif cdc == 33:
        nome_cidade = "Toledo-PR"
    elif cdc == 34:
        nome_cidade = "Cascavel-PR"
    else:
        break
    print("--- ",nome_cidade," ---")
    vP = int(input("Digite o numero de veiculos de passeio: "))
    vA = int(input("Digite o numero de Acidentes: "))            
    tv += vP
    mediaTotal = tv/12
    if(cdc >= 11 and cdc <=14):
        tvesc += vP
        mediaVEsc = tvesc/4
    if(cdc >= 21 and cdc <=24):
        tvers += vP
        mediaVErs = tvers/4
    if(cdc >= 31 and cdc <=34):
        tvepr += vP
        mediaVEpr = tvepr/4
    if vA > maiorAcidentes:
        maiorAcidentes = vA
        cm = nome_cidade  
    if vA < menorAcidentes:
        menorAcidentes = vA
        cp = nome_cidade    
    if(cdc >= 11 and cdc <=14): 
        taSC += vA  
        mediaAsc = taSC/4
    if(cdc >= 21 and cdc <=24):
        taRS += vA
    if(cdc >= 31 and cdc <=34):
        taPR += vA
print("O maior Indice de acidentes de trânsito é ", cm)
print("\nO menor Indice de acidentes de trânsito é ", cp)
print("\nA média de veículos nas cidades brasileiras no total é ", mediaTotal)   
print("\nA média de veículos em SC é ", mediaVEsc) 
print("\nA média de veículos em RS é ", mediaVErs)    
print("\nA média de veículos em PR é ", mediaVEpr)
print("\nO total de acidentes com vítimas nas cidades de SC é ", taSC)   
print("\nA média de acidentes com vítimas nas cidades do é ", mediaAsc)
print("\nO total de acidentes com vítimas nas cidades de RS é ", taRS)  
print("\nO total de acidentes com vítimas nas cidades de PR é ", taPR)  