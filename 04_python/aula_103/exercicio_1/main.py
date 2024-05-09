from funcoes import *

while(True):
    
    opcao = exibirMenu()
    limpar()

    if(opcao == 1):
        registo()
    elif(opcao == 2):
        editar()
    elif(opcao == 3):
        apagar()
    elif(opcao == 4):
        lista()
    elif(opcao == 0):
        sair()
        break    
    else:
        print("--- DADOS INVALIDOS --- ")
    
    print()
    enter()
