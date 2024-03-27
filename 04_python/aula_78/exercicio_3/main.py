import math

print()
nome = input(" Digite o nome do aluno(a): ")
nota1 = int(input(" Digite a nota da prova 1: "))
nota2 = int(input(" Digite a nota da prova 2: "))
tpc = int(input(" Digite a nota do trabalho de casa: "))
media = int(nota1 + nota2 + tpc)/3

print("O(a) aluno(a) ({}) obteve uma média final de ({:.2f}) valores.".format(nome, media))
