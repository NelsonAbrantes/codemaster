from funcoes import *

limpar()
print("\n")

quantidade = int(input(" Quantas maças comprou? "))


limpar()
analisar()

print("\n")

print(f"Comprou ( {quantidade} ) maças pelo preço todal de ( {macas(quantidade):.2f} )")

print("\n")