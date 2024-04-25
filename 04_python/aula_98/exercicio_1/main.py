from funcoes import *


while(True):
    
    opcao = menu()

    limpar()

    if(opcao == 1): venda()
    elif(opcao == 2): historico()
    elif(opcao == 3): 
        sair()
        break
    else: print("=== opção inválida ===\n".upper())

    enter()