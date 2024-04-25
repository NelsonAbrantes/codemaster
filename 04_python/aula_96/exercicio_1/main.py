from funcoes import *

print()

loop = 1

while(True):

    tentativa = input(f" Voces deseja encerrar o loop WHILE na tentativa ({loop}/5)? ")
    
    if(tentativa.lower() == "sim"):
        print() 
        print(" Voce nao ultrapassou o numero de tentativas.\n")
        break
    
    elif(loop >= 5):
        print()
        print(" Voce ultrapassou o numero de tentativas.\n")
        break
    loop += 1

    
    


