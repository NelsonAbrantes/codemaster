from funcoes import *

limpar()
print()

fruta = ["uva", "maçã", "morango", "ananás", "banana", "laranja"]

print(f"O 1º elemento é: ( {fruta[0]} )")
print()

print(f"O último elemento é 'usando indexs positivos': ( {fruta[5]} )")
print()

print(f"O último elemento é 'usando indexs negativos': ( {fruta[len(fruta)-1]} )")
print()

sublista = fruta[1:5]
print(f"A sublista contendo o 2º elemento até ao 4º: ( sublista )")
print()

fruta[1] = "clementina"

print(f"Alterar o 2º elemento por clementina: {fruta}")
print()
