import os
import time


#-- funções --

def percentagem(salario, aumento):
    resultado = salario * (1 + aumento / 100)
    return resultado

#-- funcoes especiais --

def limpar():
    if(os.name == "nt"): os.system("cls")
    else: os.system("clear")

def aguardar(tempo):
    time.sleep(tempo)