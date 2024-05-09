from funcoes import *

matriz_original = [["Nelson", 33, "Seia"], ["Maria", 14, "Lisboa"], ["Ana", 56, "Amadora"], ["Carlos", 44, "Porto"]]

limpar()

print("=== Listagem das pessoas na matriz ===\n")

for x in matriz_original:
    print(f"{x[0]} - ({x[1]}) - [{x[2]}]")

print()

