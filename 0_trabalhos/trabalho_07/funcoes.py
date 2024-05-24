import os
import time
import globais
from Produto import *
from Venda import *

# funções

def exibirMenu():
    loading()
    print("=== Loja Python ===\n")
    print("1 - Registar produto.")
    print("2 - Editar produto.")
    print("3 - Apagar produto.")
    print("4 - Lista de produtos.\n")
    print("5 - Vender.")
    print("6 - Lista das vendas.\n")
    print("0 - Sair.\n")
    return int(input("Opção: "))

def registo():
    print("--- Registar Produto---\n")
    nome = input(" Digite o NOME do novo produto: ")
    if(verificarProdutoDuplicado(nome) == False):
        preco = float(input(" Digite o PREÇO deste produto: "))
        quantidade = int(input(" Digite a quantidade deste produto: "))
        globais.produtos.append(Produto(nome, preco, quantidade))
        print("\n--- SUCESSO! ---")
    else: 
        print("\n--- ESTE PRODUTO JÁ EXISTE ---")

def editar():  
    lista()
    print()
    separador()
    print("--- Editar produto ---\n")
    id = int(input(" Digite o ID do produto que deseja editar: "))-1
    if( id >= 0 and id < len(globais.produtos)):
    
        print()
        globais.produtos[id].toString(id)

        print("\n--- Menu de Edição ---\n")
        print("1 - Nome.")
        print("2 - preco.")
        print("3 - quantidade.\n")
        print("0 - Cancelar.\n")
        opcao = int(input("Opção: "))

        if(opcao == 1):
            novo_nome = input(f" Digite o nome do PRODUTO que irá substituir ({globais.produtos[id].getNome()}) : ")
            if(verificarProdutoDuplicado(novo_nome) == False):
                globais.produtos[id].setNome(novo_nome)
                print("\n--- Alteração efetuada com sucesso ---\n")
            else:
                print("\n--- Este PRODUTO já existe ---\n")
        elif(opcao == 2):
            novo_preco = float(input(f" Digite o novo PREÇO do produto ({globais.produtos[id].getNome()})\n O PREÇO atual é de ({globais.produtos[id].getPreco()}€) : "))
            globais.produtos[id].setPreco(novo_preco)
            print("\n--- Alteração efetuada com sucesso ---\n")
        elif(opcao == 3):
            nova_quantidade = int(input(f" Digite a nova QUANTIDADE do produto ({globais.produtos[id].getNome()})\n A QUANTIDADE atual é de ({globais.produtos[id].getQuantidade()} Unidades) : "))
            globais.produtos[id].setQuantidade(nova_quantidade)
            print("\n--- Alteração efetuada com sucesso ---\n")
        else:
            print("\n--- OPÇÃO INVÁLIDA ---")
    else:
        print("\n--- ID INVÁLIDO ---")

def apagar():
    lista()
    print()
    separador()
    print("--- Apagar Produto ---\n")
    id = int(input("Digite o ID do Produto que deseja apagar: "))-1
    confirmacao = input(f"\nTem a certesa que deseja apagar o produto ( {globais.produtos[id].getNome()} ) ? ")
    if( id >= 0 and id < len(globais.produtos) and confirmacao == "sim"):
        produto_apagado = globais.produtos[id].getNome()
        globais.produtos.pop(id)
        print(f"\n--- ( {produto_apagado} ) APAGADO COM SUCESSO ---\n")
    else:
        print("--- DADOS INVÁLIDOS ---\n")

def vender():
    lista()
    print()
    separador()
    print("--- Vender produto ---\n")
    id = int(input(" Digite o ID do produto que deseja vender: "))-1
    if( id >= 0 and id < len(globais.produtos)):
        quantidadeVendida = int(input(f" Digite a quantidade de ({globais.produtos[id].getNome()}) que será vendida: "))
        if(quantidadeVendida <= globais.produtos[id].getQuantidade() and quantidadeVendida > 0):
            globais.produtos[id].setQuantidade(globais.produtos[id].getQuantidade() - quantidadeVendida)
            globais.vendas.append(Venda(quantidadeVendida, globais.produtos[id].getNome(), globais.produtos[id].getPreco()))
            print(f"\n Venda efetuada - {globais.produtos[id].getNome()} ({globais.produtos[id].getPreco():.2f}€) X ({quantidadeVendida} uni.) = {globais.produtos[id].getPreco() * quantidadeVendida:.2f}€")
            print("\n--- SUCESSO ---")
        else: print("\n--- QUANTIDADE INVÁLIDA ---")
    else: print("\n--- ID INVÁLIDO ---")

def historicoVendas():
    print("--- Historico de vendas ---\n")
    total_vendas = 0
    for i in range(len(globais.vendas)): 
        globais.vendas[i].toString(i)
        total_venda = globais.vendas[i].getPreco() * globais.vendas[i].getQuantidade()
        print(f"\n-Total da venda: {total_venda:.2f}€\n")
        total_vendas += total_venda
        separador() 
    print(f"O total acumulado de todas as vendas é de {total_vendas:.2f} €")

def lista():
    print("--- Lista de produtos registados ---\n")    
    for i in range(len(globais.produtos)): globais.produtos[i].toString(i)

# Helpers

def iniciar():
    globais.produtos.append(Produto("Papel A5", 3.55, 32))
    globais.produtos.append(Produto("Caneta Azul", 1.25, 20))
    globais.produtos.append(Produto("Mesa", 49.99, 5))
    globais.produtos.append(Produto("Cadeira", 129.99, 25))

def verificarProdutoDuplicado(nome_a_verificar):
    for n in globais.produtos:
        if(n.produtoDuplicado(nome_a_verificar)):
            return True
    return False

# funcoes especiais

def separador():
    print("=" * 60)
    print()

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