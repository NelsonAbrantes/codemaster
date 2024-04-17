import os
import time

#-- funções --

def valorFinal (combustivel, quantidade):
    alcool = 2.90

    if(combustivel == "a"):
        if(quantidade <= 20):
            desconto = alcool * (0.97)
        else: desconto = alcool * (0.95)    
       

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