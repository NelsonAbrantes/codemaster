from funcoes import *

limpar()

salario_atual = float(input(" Digite o seu salario: "))
aumento = float(input(" Digite a percentagem do aumento: "))


print(f" O novo salario é de ( {percentagem(salario_atual, aumento):.2f} )")
