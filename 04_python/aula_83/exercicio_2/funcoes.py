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
    print("C\n", end="", flush=True)
    aguardar(tempo)
    print("o\n", end="", flush=True)
    aguardar(tempo)
    print("d\n", end="", flush=True)
    aguardar(tempo)
    print("e\n", end="", flush=True)
    aguardar(tempo)
    print("M\n", end="", flush=True)
    aguardar(tempo)
    print("a\n", end="", flush=True)
    aguardar(tempo)
    print("s\n", end="", flush=True)
    aguardar(tempo)
    print("t\n", end="", flush=True)
    aguardar(tempo)
    print("e\n", end="", flush=True)
    aguardar(tempo)
    print("r\n", end="", flush=True)
