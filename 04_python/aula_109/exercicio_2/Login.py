class login:

    def __init__(self, nome, username, password):
        self.nome = nome
        self.username = username
        self.password = password

    def toString(self):
        print(f"{self.nome:<10} ->  (Login: {self.username:>10}) (Senha: {self.password:>10})")

    def userExist(self, username_a_verificar):
        if(self.username == username_a_verificar): return True
        else: return False
    
    