from funcoes import *

limpar()
print("\n")

nota_1 = float(input(" Digite a sua primeira nota: "))
nota_2 = float(input(" Digite a sua segunda nota: "))
nota_3 = float(input(" Digite a sua terceira nota: "))

limpar()
analisar()

print("\n")

print(f" A sua média é de ( {mediafinal(nota_1, nota_2, nota_3)} )")

print("\n")