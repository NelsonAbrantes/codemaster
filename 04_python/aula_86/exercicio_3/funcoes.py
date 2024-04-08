import os
import time


#-- funções --

def macas(quantidade):

    meia_duzia = 1.30
    duzia = 1.00

    if quantidade <= 12:
        return quantidade * 1.30
    else:
        return quantidade * 1.00



#-- funcoes especiais --

def analisar():
    tempo = 0.8
    limpar()
    print("A analisar.")
    aguardar(tempo)
    limpar()
    print("A analisar..")
    aguardar(tempo)
    limpar()
    print("A analisar...")
    aguardar(tempo)
    limpar()

def limpar():
    if(os.name == "nt"): os.system("cls")
    else: os.system("clear")

def aguardar(tempo):
    time.sleep(tempo)