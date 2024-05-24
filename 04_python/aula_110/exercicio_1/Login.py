class login:

    def __init__(self, nome, username, password):
        self.nome = nome
        self.username = username
        self.password = password

    def toString(self):
        print(f"{self.nome:<10} ->  (Login: {self.username:>10}) (Senha: {self.password:>10})")

    def userExiste(self, verificar_username, verificar_password):
        if(self.username == verificar_username) and (self.password == verificar_password): return True
        else: return False

    def getLogin 