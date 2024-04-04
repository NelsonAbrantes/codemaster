from funcoes import *

limpar()

nome = input(" Digite o seu nome: ")
idade = int(input(" Digite a sua idade: "))
conhecimentos = input(" Tem conhecimentos em programação? ")

limpar()
analisar()

print("=== Ficha de candidatura ===\n")
print(f"Nome: ( {nome} )\nidade: ( {idade} )\nStatus da candidatura: ( {candidatura(idade, conhecimentos)} )")
