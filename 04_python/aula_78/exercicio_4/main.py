
import math

nome = input(" Digite o nome do(a) paciente: ")
peso = int(input(" Digite o peso do(a) paciente (kg): "))
altura = float(input(" Digite o altura do(a) paciente (m): "))
imc = peso / (altura ** 2)

print(f"O(a) paciente ({nome}) está com um IMC de ({imc}) .")