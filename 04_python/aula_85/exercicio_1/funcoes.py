import os
import time


#-- funções --

def calcular_percentagem(total, valor):
    resultado = (valor / total) * 100
    return resultado




#-- funcoes especiais --

def limpar():
    if(os.name == "nt"): os.system("cls")
    else: os.system("clear")

def aguardar(tempo):
    time.sleep(tempo)