import os
import time

def arearetangulo(altura , base):

    area = base * altura
    print(f"A área do retângulo é de {area}")




#-- funcoes especiais --

def limpar():
    if(os.name == "nt"): os.system("cls")
    else: os.system("clear")

def aguardar(tempo):
    time.sleep(tempo)
