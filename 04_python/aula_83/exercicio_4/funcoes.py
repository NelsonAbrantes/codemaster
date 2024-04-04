import os
import time

def desconto(preco):
    novo_preco = preco * 0.9
    print(f"O novo preco é de {novo_preco} Euros.")

def desconto_2(preco):
    novo_preco = preco * 0.9
    return novo_preco


def limpar():
    if(os.name == "nt"): os.system("cls")
    else: os.system("clear")

def aguardar(tempo):
    time.sleep(tempo)
