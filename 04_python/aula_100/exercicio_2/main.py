from funcoes import *

print()
limpar()

frutas = ['uva', 'maçã', 'morango', 'ananás', 'banana', 'laranja']

print(f"Lista original: {frutas}")

print("--- Lista de Frutas com FOR ---\n")
for f in frutas: print(f)
print()

print("--- Lista de Frutas com FOR + RANGE ---\n")
for f in range(len(frutas)): print(f"{f +1 } - {frutas[f]}")
print()

print("--- Lista de Frutas com FOR + REVERSE ---\n")
for f in reversed(frutas): print(f)
print()

print("--- Lista de Frutas com FOR + RANGE REVERSE ---\n")
for f in range(len(frutas)-1, -1, -1): print(f"{f + 1} - {frutas[f]}")
print()

