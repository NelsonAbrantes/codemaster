import os
import re
import time
import globais

#-- funções --

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
    preco = float(input(" Digite o PREÇO deste produto: "))
    quantidade = int(input(" Digite a quantidade deste produto: "))
    globais.produtos.append(novoProduto(nome, preco, quantidade))
    print("\n--- SUCESSO! ---")

def editar():  
    lista()
    print()
    print("=" * 40)
    print("\n--- Editar produto ---\n")
    id = int(input(" Digite o ID do produto que deseja editar: "))-1
    if( id >= 0 and id < len(globais.produtos)):
    
        print()
        exibirProduto(id)

        print("\n--- Menu de Edição ---\n")
        print("1 - Nome.")
        print("2 - preco.")
        print("3 - quantidade.\n")
        print("0 - Cancelar.\n")
        opcao = int(input("Opção: "))

        if(opcao == 1):
            novo_nome = input(f" Digite o novo PRODUTO que ira substituir [ {globais.produtos[id] ['nome']} ]: ")
            if(verificarProdutoDuplicado(novo_nome) == False):
                globais.produtos[id]  ['nome'] = novo_nome
                print("\n--- Alteração efetuada com sucesso ---\n")
            else:
                print("\n--- Este PRODUTO já existe ---\n")
        elif(opcao == 2):
            globais.produtos[id] ['preco'] = float(input(f" Digite o novo PREÇO que substituirá ({globais.produtos[id] ['preco']}): "))
            print("\n--- Alteração efetuada com sucesso ---\n")
        elif(opcao == 3):
            globais.produtos[id] ['quantidade'] = int(input(f" Digite a QUANTIDADE que substituirá ({globais.produtos[id] ['quantidade']}): "))
            print("\n--- Alteração efetuada com sucesso ---\n")
        elif(opcao == 0):
            print("\n--- Operação cancelada! ---")
        else:
            print("\n--- OPÇÃO INVÁLIDA ---")

def apagar():
    lista()
    print()
    print("=" * 40)
    print("\n--- Apagar Produto ---\n")
    id = int(input("Digite o ID do Produto que deseja apagar: "))-1
    confirmacao = input(f"\nTem a certesa que deseja apagar o produto ( {globais.produtos[id] ['nome']} ) ? ")
    if( id >= 0 and id < len(globais.produtos) and confirmacao == "sim".lower()):
        produto_apagado = globais.produtos[id] ['nome']
        globais.produtos.pop(id)
        print(f"\n--- ( {produto_apagado} ) APAGADO COM SUCESSO ---\n")
    else:
        print("--- DADOS INVÁLIDOS ---\n")

def vender():
    lista()
    print()
    print("=" * 40)
    print("\n--- Vender produto ---\n")
    id = int(input(" Digite o ID do produto que deseja vender: "))-1
    if( id >= 0 and id < len(globais.produtos)):
        v = globais.produtos[id]
        quantidadeVenda = int(input(f" Digite a quantidade de ({v ['nome']}) que será vendida: "))
        if(quantidadeVenda <= v['quantidade'] and quantidadeVenda > 0):
            v['quantidade'] -= quantidadeVenda
            globais.vendas.append(novaVenda(v["nome"],v["preco"] ,quantidadeVenda ))
            print(f"\n Venda efetuada - {v ['nome']} ({v["preco"]}€) X ({quantidadeVenda} uni.) = {v['preco'] * quantidadeVenda:.2f}€")
            print("\n--- SUCESSO ---")
        else: print("\n--- QUANTIDADE INVÁLIDA ---")
    else: print("\n--- ID INVÁLIDO ---")

def historicoVendas():
    print("--- Historico de vendas ---\n")
    for v in globais.vendas:
        print(f"Nome: ({v['nome']}) | Preço: ({v['preco']:.2f}€)| Quantidade: ({v['quantidade']})")
        total = v['preco'] * v['quantidade']
        print(f"-Total das vendas: {total:.2f}€\n")
        print("=" * 40)
        print()
    totalVendas = (v['preco'] * v['quantidade'] for v in globais.vendas)
    print(f"O total acumulado de todas as vendas é de {totalVendas} €")

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

def novaVenda(nome, preco, quantidade):
    nova_venda ={
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    return nova_venda

def exibirProduto(id):
    p = globais.produtos[id]
    print(f"#{id + 1} - NOME: ({p['nome']}) | preço: ({p['preco']:.2f}€) | quantidade: ({p['quantidade']})")

def verificarProdutoDuplicado(novo_nome):
    for n in globais.produtos:
        if(n['nome'].lower() == novo_nome.lower()):
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