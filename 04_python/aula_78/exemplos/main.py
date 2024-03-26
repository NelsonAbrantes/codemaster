
import math

numero = int(input(" Digite um número inteiro: "))
dobro = numero * 2

print(f"O dobro do numero ({numero}) é igual a ({dobro})")



ano_atual = 2024
idade = int(input(" Digite a sua idade: "))
ano_nasc = ano_atual - idade

print(f"Você nasceu em ({ano_nasc})")



nome = input(" Digite o seu nome: ")
nif = input(" Digite o seu NIF: ")
morada = input(" Digite a sua morada: ")
altura = float(input(" Digite a sua altura: "))

print(f"Nome: {nome}")
print(f"NIF: {nif}")
print(f"Morada: {morada}")
print("Altura: ({:.2f} m).".format(altura))