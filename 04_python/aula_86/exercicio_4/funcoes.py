import os
import time

#-- funções --

def tempo(inicio, fim):
    
    duracao = fim - inicio

    if(duracao == 0):
        return print("A duração foi de 24 horas.")
    elif(duracao > 24):
        return print("A duraçao nao pode ultrapassar as 24 Horas")
    else:
        return print(f"A duração foi de {duracao} horas")

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