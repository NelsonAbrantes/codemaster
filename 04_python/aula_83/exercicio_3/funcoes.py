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
    print("{:>2}".format("o"))
    aguardar(tempo)
    print("{:>3}".format("d"))
    aguardar(tempo)
    print("{:>4}".format("e"))
    aguardar(tempo)
    print("{:>5}".format("M"))
    aguardar(tempo)
    print("{:>6}".format("a"))
    aguardar(tempo)
    print("{:>7}".format("s"))
    aguardar(tempo)
    print("{:>8}".format("t"))
    aguardar(tempo)
    print("{:>9}".format("e"))
    aguardar(tempo)
    print("{:>10}".format("r"))
    aguardar(tempo)

