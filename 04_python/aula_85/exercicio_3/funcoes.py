import os
import time


#-- funções --

def mediafinal(n1, n2, n3):
    media = (n1 * 2 + n2 * 3 + n3 * 5) / 10
    return media


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