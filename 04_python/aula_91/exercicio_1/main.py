from funcoes import *

limpar()

loop = 1
while(loop <= 10):
    print(loop)
    loop += 1

print()

resposta = ""
while(resposta.lower() != "sim"):
    resposta = input(" Voce deseja sair do loop? ")

print()

resposta = ""
saldo = 0
dias = 1
while(resposta.lower != "nao and saldo < 20"):
    resposta = input(f"No ({dias}), está a chover? ")
    saldo = float(input(f"No ({dias}), qual é o teu saldo? "))
    print()
    dias += 1








resposta = ""
tentativas = 0
while(resposta.lower() != "sim" and tentativas < 3 ):
    resposta = input("Você passou no teste oral: ")
    tentativas += 1

print("\n")