class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def toString(self, id):
        print(f"#{id + 1} - NOME: {self.nome:>13} | PREÇO: {self.preco:>7.2f}€ | QUANTIDADE: {self.quantidade:>4}")

    def produtoDuplicado(self, nome_a_verificar):
        if self.nome.lower() == nome_a_verificar.lower():
            return True
        else: return False

    def setNome(self, novo_nome):
        self.nome = novo_nome

    def setPreco(self, novo_preco):
        self.preco = novo_preco

    def setQuantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade 

    def getNome(self):
        return self.nome

    def getPreco(self):
        return self.preco

    def getQuantidade(self):
        return self.quantidade 

