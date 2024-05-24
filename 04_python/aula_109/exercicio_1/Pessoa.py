class pessoa:

    def __init__(self, nome, idade, morada, nif):
        self.nome = nome
        self.idade = idade
        self.morada = morada
        self.nif = nif

    def toString(self):
        print(f"{self.nome:<15} -> (Idade: {self.idade:>2}) (Morada: {self.morada:>8}) (NIF: {self.nif:>5})")
    
    def aniversario(self):
        self.idade += 1
        print(f"{self.nome} fez {self.idade} anos!!")
        
    def mudancaMorada(self, novaMorada):
        print(f"{self.nome} mudou-se de ({self.morada:<10} -> {novaMorada:>10})")
        self.morada = novaMorada


