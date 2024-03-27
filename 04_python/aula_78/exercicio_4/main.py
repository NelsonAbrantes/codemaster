
import math

nome = input(" Digite o nome do(a) paciente: ")
peso = float(input(" Digite o peso do(a) paciente (kg): "))
altura = float(input(" Digite o altura do(a) paciente (m): "))
imc = peso / (altura ** 2)

print("O(a) paciente ({}) está com um IMC de ({:.2f}) .".format(nome, imc))