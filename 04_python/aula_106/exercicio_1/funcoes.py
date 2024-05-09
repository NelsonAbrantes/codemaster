import os
import time
import globais

#-- funções --

def exibirMenu():
    loading()
    print("=== Loja Python ===\n")
    print("1 - Registar produto.")
    print("2 - Editar produto.")
    print("3 - Apagar produto.")
    print("4 - Listar produtos.\n")
    print("5 - Vender.")
    print("6 - Listar vendas.\n")
    print("0 - Sair.\n")
    return int(input("Opção: "))

def registo():
    print("--- Registar Prato---\n")
    nome = input(" Digite o NOME do novo produto: ")
    preco = float(input(" Digite o PREÇO deste produto: "))
    quantidade = int(input(" Digite a quantidade deste produto: "))
    globais.produtos.append(novoProduto(nome, preco, quantidade))
    print("--- SUCESSO! ---")


def lista():
    print("--- Lista de produtos registados ---\n")    
    for i in range(len(globais.produtos)): exibirProduto(i)
    
# Helpers

def init():
    globais.produtos.append(novoProduto("Papel A5", 3.55, 32))
    globais.produtos.append(novoProduto("Caneta Azul", 1.25, 20))
    globais.produtos.append(novoProduto("Mesa", 49.99, 5))
    globais.produtos.append(novoProduto("Cadeira", 129.99, 25))

def novoProduto(nome, preco, quantidade):
    novo_Produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    return novo_Produto

def exibirProduto(id):
    p = globais.produtos[id]
    print(f"ID: ( {id + 1} ) | NOME: ( {p['nome']} ) | preço: ( {p['preco']:.2f} €) | quantidade: ( {p['quantidade']} )")


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