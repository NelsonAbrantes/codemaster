import os
import time
import globais

#-- funções --

def exibirMenu():
    loading()
    print("=== Gestão de Colaboradores ===\n")
    print("1 - Novo colaborador.")
    print("2 - Editar colaborador.")
    print("3 - Apagar colaborador.")
    print("4 - Listar todos os colaboradores.\n")
    print("0 - Sair.\n")
    return int(input("Opção: "))

def registo():
    print("--- Novo Colaborador ---\n")
    nome = input(" Digite o NOME do novo colaborador(a): ")
    cargo = input(" Digite o CARGO do novo colaborador(a): ")
    ordenado = ""

    while(ordenado.isnumeric() == False):
        
        ordenado = int(input(" Digite o ORDENADO do novo colaborador(a): "))

        if(ordenado.isnumeric() == True):
            print("\n--- Registo concluido com Sucesso ---\n")
        else: 
            print("\n--- INSIRA UM VALOR NUMÉRICO NO CAMPO ORDENADO ---\n")
              
    novo_colaborador = [nome, cargo, ordenado]
    globais.colaboradores.append(novo_colaborador)


def editar():  
    lista()
    print()
    print("=" * 40)
    print("\n--- Editar Colaborador ---\n")
    id = int(input(" Digite o ID do colaborador que deseja editar: "))
    if( id >= 0 and id < len(globais.colaboradores)):

        print("\n--- Menu de Edição ---\n")
        print("1 - Nome.")
        print("2 - Cargo.")
        print("3 - Ordenado.\n")
        print("0 - Cancelar.\n")
        opcao = int(input("Opção: "))

        if(opcao == 1):
            novo_nome = input(f" Digite o novo NOME que ira substituir [ {globais.colaboradores[id] [0]} ]: ")
            if(verificarNomeExistente(novo_nome) == False):
                globais.colaboradores[id] [0] = novo_nome
                print("\n--- Alteração efetuada com sucesso ---\n")
            else:
                print("\n--- Este NOME já existe ---\n")
        elif(opcao == 2):
            globais.colaboradores[id] [1] = (input(f" Digite o novo CARGO que substituirá ({globais.colaboradores[id] [1]}): "))
        elif(opcao == 3):
            globais.colaboradores[id] [2] = int(input(f" Digite o ORDENADO que substituirá ({globais.colaboradores[id] [2]}): "))
        elif(opcao == 0):
            print("\n--- Operação cancelada! ---")
        else:
            print("\n--- OPÇÃO INVÁLIDA")

def apagar():
    lista()
    print()
    print("=" * 40)
    print("\n--- Apagar Colaborador ---\n")
    id = int(input("Digite o ID do colaborador que deseja apagar: "))
    confirmacao = input(f" Tem a certesa que deseja apagar a pessoa ( {globais.colaboradores[id] [0]} ) ? ")
    if( id >= 0 and id < len(globais.colaboradores) and confirmacao == "sim".lower()):
        pessoa_apagada = globais.colaboradores[id] [0]
        globais.colaboradores.pop(id)
        print(f"\n--- ( {pessoa_apagada} ) APAGADO COM SUCESSO ---\n")
    else:
        print("--- DADOS INVÁLIDOS ---\n")            

def lista():
    print("--- Lista de Colaboradores registados ---\n")
    total_ordenado = 0       
    for i in range(len(globais.colaboradores)):
        print(f"ID: ( {i} ) | NOME: ( {globais.colaboradores[i] [0]} ) | Cargo: ( {globais.colaboradores[i] [1]} ) | Ordenado: ( {globais.colaboradores[i] [2]} )")
    print(f"\nTotal de colaboradores: ( {len(globais.colaboradores)} )\n")
    total_ordenado += globais.colaboradores[2]
    print(f"O ordenado total mensal da equipa é de ( {total_ordenado} ).")           


# Helpers

def verificarNomeExistente(novo_nome):
    for n in globais.colaboradores:
        if(n[0].lower() == novo_nome.lower()):
            return True
    return False


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