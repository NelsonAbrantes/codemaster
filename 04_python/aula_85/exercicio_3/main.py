from funcoes import *

limpar()

nota_1 = float(input(" Digite a sua primeira nota: "))
nota_2 = float(input(" Digite a sua segunda nota: "))
nota_3 = float(input(" Digite a sua terceira nota: "))

limpar()
analisar()

print(f" A sua média é de ( {mediafinal(nota_1, nota_2, nota_3)} )")

