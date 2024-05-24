class Venda:

    def __init__(self, quantidade, nome_produto, preco_produto):
        self.quantidade = quantidade
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto
    
    def toString(self, id):
        print(f"Venda #{id + 1} - NOME: ({self.nome_produto}) | PREÇO: ({self.preco_produto:.2f}€) | QUANTIDADE: ({self.quantidade})") 

    def getPreco(self):
        return self.preco_produto

    def getQuantidade(self):
        return self.quantidade 