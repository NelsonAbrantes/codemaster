from funcoes import *

limpar()
print()

total_alunos = int(input(" Digite o total alunos a serem registados: "))
alunos = []

print()

for i in range(total_alunos):
    novo_aluno = input(f" Digite o nome do(a) ( {i + 1} º) aluno(a): ")
    alunos.append(novo_aluno)


limpar()

i = 1
alunos.sort()
print("--- Lista Ordenada de Alunos ---\n")
for z in alunos: 
    print(f"{i} - {z}.")
    i += 1

print()