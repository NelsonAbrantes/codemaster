import os
import time


#-- funções --

def resposta(valor):
    if valor  >= 10:
        return print(" é maior que 10!".upper())
    else:
        return print(" não é maior que 10!".upper())
    


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