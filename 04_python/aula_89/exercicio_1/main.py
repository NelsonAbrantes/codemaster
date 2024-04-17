from funcoes import *

limpar()
print("\n")

print("=== Cálculo de Áreas com funções ===\n")
print("--- Escolha uma opção ---\n\n (t) para triangulos\n (r) para rectangulos\n (c) para circulo\n" )
opcao = input("Opçao: ")

limpar()
print("\n")

if opcao == "t":
    triangulo()
    print()
elif opcao == "r":
    retangulo()
    print()
elif opcao == "c":
    circulo()
    print()
else: print("-- Opção Inválida --")
