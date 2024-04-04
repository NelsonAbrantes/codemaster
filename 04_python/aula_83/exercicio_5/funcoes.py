import os
import time

#-- funcoes --

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

def candidatura(idade, conhecimentos):

    if(idade >= 18 and conhecimentos.lower() == "sim"):
        return "Aprovado para estágio".upper()
    if(idade <= 18 and conhecimentos.lower() == "sim"):
        return "Aprovado para escola de Programadores".upper()
    if(idade >= 18 and conhecimentos.lower() == "nao"):
        return "Não Aprovado para estágio".upper()
    if(idade <= 18 and conhecimentos.lower() == "nao"):
        return "Não aprovado para escola de programadores".upper()
    else:
        return "Erro nos dados informados, tente novamente".upper()
    
       
#-- funcoes especiais --
def limpar():
    if(os.name == "nt"): os.system("cls")
    else: os.system("clear")

def aguardar(tempo):
    time.sleep(tempo)

