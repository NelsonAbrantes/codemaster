from funcoes import *

opcao = None

while(True):
    
    opcao = menu()

    limpar()

    if(opcao == 1): levantamentos()
    elif(opcao == 2): depositos()
    elif(opcao == 3): pagamentos()
    elif(opcao == 4): historico()
    elif(opcao == 5): break
    else: print("=== opção inválida ===".upper())

    enter()