
print()
print(" === Escola Codemaster ===\n")

total_alunos = int(input(" Digite o numero de alunos: "))
idade_total = 0
alunos = 1

print()

while(alunos <= total_alunos):
    idade = int(input(f" Digite a idade do aluno ( {alunos} ): "))   
    idade_total += idade
    alunos += 1

media = idade_total / alunos

print(f" A média de idades da turma é de ( {media:.1f} ).")