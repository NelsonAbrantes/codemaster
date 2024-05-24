import os
import re
import time

#-- funções --



# Helpers

# def init():
#     globais.produtos.append(novoProduto("Papel A5", 3.55, 32))
#     globais.produtos.append(novoProduto("Caneta Azul", 1.25, 20))
#     globais.produtos.append(novoProduto("Mesa", 49.99, 5))
#     globais.produtos.append(novoProduto("Cadeira", 129.99, 25))

# def novoProduto(nome, preco, quantidade):
#     novo_Produto = {
#         "nome": nome,
#         "preco": preco,
#         "quantidade": quantidade
#     }
#     return novo_Produto

# def novaVenda(nome, preco, quantidade):
#     nova_venda ={
#         "nome": nome,
#         "preco": preco,
#         "quantidade": quantidade
#     }
#     return nova_venda

# def exibirProduto(id):
#     p = globais.produtos[id]
#     print(f"#{id + 1} - NOME: ({p['nome']}) | preço: ({p['preco']:.2f}€) | quantidade: ({p['quantidade']})")

# def verificarProdutoDuplicado(novo_nome):
#     for n in globais.produtos:
#         if(n['nome'].lower() == novo_nome.lower()):
#             return True
#     return False

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