mediaTurma = 0.0
alunosA7 = 0
nota = 0
alunos = 0
notas = 0.0
for i in range(35):
    nomealuno = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota dele: "))
    alunos += 1
    notas += nota

    if nota >7:
        alunosA7 += 1

    print(nomealuno, "nota ",nota)

print("A media da turma foi: ",notas/alunos)
print("\n",alunosA7, "Alunos tiraram acima de 7")