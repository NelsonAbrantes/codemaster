import os
import time

def limpar():
    if(os.name == "nt"): os.system("cls")
    else: os.system("clear")

def aguardar(tempo):
    time.sleep(tempo)

def esperar():
    tempo = 0.5
    limpar()
    print("C")
    aguardar(tempo)
    limpar()
    print("Cod")
    aguardar(tempo)
    limpar()
    print("CodeM")
    aguardar(tempo)
    limpar()
    print("CodeMaster")
    aguardar(tempo)
