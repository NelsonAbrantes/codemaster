from Login import login
from funcoes import *

p1 = login("Nelson", "nelson_10", "qqrcoisa")
p2 = login("Maria", "maria9", "codigo")
p3 = login("André", "andre72", "aspirador_1")
todos = [p1,p2,p3]


limpar()
print("\n=== Lista Original ====\n")

login.toString(p1)
login.toString(p2)
login.toString(p3)

print("\n")

username_a_verificar = input("Username: ")
password_a_verificar = input("Password: ")
print()





   


print("\n")