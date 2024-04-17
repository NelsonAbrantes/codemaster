import os
import time
import math

#-- funções --

def triangulo():
     
    base = int(input(" Digite a medida da base: "))
    altura = int(input(" Digite a Altura: "))
    resultado = (base * altura) / 2
    analisar()
    print(f"A area do triangulo é de ( {resultado} ).")

    
def retangulo():
     
    base = int(input(" Digite a medida da base: "))
    altura = int(input(" Digite a Altura: "))
    resultado = base * altura
    analisar()
    print(f"A area do retangulo é de ( {resultado} ).")


def circulo():
     
    raio = int(input(" Digite a medida do raio: "))
    resultado = math.pi * (raio ** 2)
    analisar()
    print(f"A area do circulo é de ( {resultado:.2f} ).")       



#-- funcoes especiais --

def analisar():
    tempo = 0.7
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