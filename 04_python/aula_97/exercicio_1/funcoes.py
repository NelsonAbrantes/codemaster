import os
import time
import globais

#-- funções --

def enter():
    input(" Carregue <ENTER> para continuar...")


def menu():
    loading()
    print("=== Multibanco python ===\n")
    print("Conta: Nelson")
    print(f"Saldo: {globais.saldo}")
    print("\n")
    print("1 - Levantamentos.")
    print("2 - Depósitos.")
    print("3 - Pagamentos.")
    print("\n")
    print("4 - Histórico")
    print("5 - Sair")
    print("\n")
    return int(input("- Opção: "))

def historico():
    print("--- Histórico ---")
    print(globais.historico)
    globais.historico += "verificou o Histórico\n"

def levantamentos():
    print("--- Levantamentos ---\n")
    quantia = int(input("- Valor a ser levantado: "))
    if(quantia <= globais.saldo and quantia > 0):
        globais.saldo -= quantia
        print("--- SUCESSO! ---")
        globais.historico += f"-Levantou: {quantia}\n"
    else:
        print("--- QUANTIDADE INVÁLIDA ---")


def depositos():
    print("--- Depósitos ---\n")
    quantia = int(input("- Valor a ser depositado: "))
    if(quantia > 0):
        globais.saldo += quantia
        print("--- SUCESSO! ---") 
        globais.historico += f"-Depositou: {quantia}\n"       
    else:
        print("--- QUANTIDADE INVÁLIDA ---")


def pagamentos():
    print("--- Pagamentos ---\n")
    descricao = input("Descrição do pagamento: ")
    quantia = int(input("- Valor do pagamento: "))
    if(quantia <= globais.saldo and quantia > 0):
        globais.saldo -= quantia
        print("--- SUCESSO! ---")
        globais.historico += f"-Pagamento de: {quantia} motivo: {descricao}\n"        
    else:
        print("--- QUANTIDADE INVÁLIDA ---")


#-- funcoes especiais --


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