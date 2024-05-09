from funcoes import *

matriz_original = [["morango", "banana", "uva"],["frango", "bifana", "novilho"], ["agua", "cola", "pepsi"]]

limpar()
print()

print("=== For para cada lista dentro da matriz ===\n")

for l in matriz_original:
    print(l)
print()

print("=== For para cada item dentro de cada lista da matriz ===\n")

for x in matriz_original:
    for y in x:
        print(y)
    print()

print()