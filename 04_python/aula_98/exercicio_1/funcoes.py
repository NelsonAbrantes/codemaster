import os
import time
import globais

#-- funções --

def enter():
    input(" Carregue <ENTER> para continuar...")

def menu():
    loading()
    print("=== Padaria do python ===\n")
    print("1 - Vender.")
    print("2 - Ver histórico.")
    print("3 - Sair.\n")
    return int(input("- Opção: "))

def historico():
    print("--- Histórico ---\n")
    print(f"Total de vendas: {globais.saldo:.2f} €\n")
    print(globais.historico)

def venda():
    print("--- Vender ---\n")
    descricao = input("Descrição da Venda: ")
    quantia = int(input("- Valor total da venda: "))
    if(quantia > 0):
        print("\n--- SUCESSO! ---")
        globais.saldo += quantia
        globais.historico += f"{descricao} - {quantia:.2f} €\n"
        print()          
    else:
        print("--- QUANTIDADE INVÁLIDA ---")


#-- funcoes especiais --

def sair():
    tempo = 0.5
    limpar()
    print("A Sair.", end="", flush=True)
    aguardar(tempo)
    limpar()
    print("A Sair..", end="", flush=True)
    aguardar(tempo)
    limpar()
    print("A Sair...", end="", flush=True)
    aguardar(tempo)
    limpar()
    

def loading():
    tempo = 0.5
    limpar()
    print("Aguardar.", end="", flush=True)
    aguardar(tempo)
    limpar()
    print("Aguardar..", end="", flush=True)
    aguardar(tempo)
    limpar()
    print("Aguardar...", end="", flush=True)
    aguardar(tempo)
    limpar()


def limpar():
    if(os.name == "nt"): os.system("cls")
    else: os.system("clear")



def aguardar(tempo):
    time.sleep(tempo)