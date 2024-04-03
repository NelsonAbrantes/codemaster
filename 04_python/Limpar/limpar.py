import os
def limpar():
    if(os.name == "nt"): os.system("cls")
    else: os.system("clear")