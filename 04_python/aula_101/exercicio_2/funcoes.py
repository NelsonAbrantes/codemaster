import os
import time
import globais

#-- funções --

def exibirMenu():
    loading()
    print("=== Registo de Pessoas ===\n")
    print("1 - Registar nova pessoa.")
    print("2 - Editar pessoa.")
    print("3 - Apagar pessoa.")
    print("4 - Lista de todas as pessoas registadas.\n")
    print("0 - Sair.\n")
    return int(input("Opção: "))

def registo():
    print("--- Registo de pessoas ---\n")
    nova_pessoa = input(" Digite o nome da nova pessoa: ")
    globais.pessoas.append(nova_pessoa)
    print("\n--- Registo concluido com Sucesso ---\n")

def editar():  
    lista()
    print()
    print("=" * 40)
    print("\n--- Editar Nome ---\n")
    id = int(input(" Digite o ID da pessoa que deseja editar: "))
    if( id >= 0 and id < len(globais.pessoas)):
        novo_nome = input(f" Digite o novo nome que ira substituir [ {globais.pessoas[id]} ]: ")
        globais.pessoas[id] = novo_nome
        print("\n--- Alteração efetuada com sucesso ---\n")
    else:
        print("\n--- ID Inválido ---\n")

def apagar():
    lista()
    print()
    print("=" * 40)
    print("\n--- Apagar Pessoa ---\n")
    id = int(input(" Digite o ID da Pessoa que deseja apagar: "))
    confirmacao = input(f"Tem a certesa que deseja apagar a pessoa ( {globais.pessoas[id]} ) ? ")
    if( id >= 0 and id < len(globais.pessoas) and confirmacao == "sim".lower()):
        pessoa_apagada = globais.pessoas[id]
        globais.pessoas.pop(id)
        print(f"\n--- ( {pessoa_apagada} ) APAGADO COM SUCESSO ---\n")
    else:
        print("--- DADOS INVALIDO ---\n")            

def lista():
    print("--- Lista das pessoas registadas ---\n")         
    for i in range(len(globais.pessoas)):
        print(f"ID: ( {i} ) - NOME: ( {globais.pessoas[i]} )")



#-- funcoes especiais --

def enter():
    input(" Carregue <ENTER> para continuar...")

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
    tempo = 0.4
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