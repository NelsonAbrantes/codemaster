from Pessoa import *
from funcoes import *


p1 = pessoa("Nelson", 54, "Seia", 111)
p2 = pessoa("Maria", 14, "Lisboa", 222)
p3 = pessoa("Carolina", 36, "Faro", 333)
p4 = pessoa("Carlos", 44, "Porto", 444)
p5 = pessoa("Gustavo", 56, "Coimbra", 555)

limpar()
print("\n=== Lista Original ====\n")

pessoa.toString(p1)
pessoa.toString(p2)
pessoa.toString(p3)
pessoa.toString(p4)
pessoa.toString(p5)

print("\n")

pessoa.aniversario(p1)
pessoa.aniversario(p2)
pessoa.aniversario(p3)

print("\n")
pessoa.mudancaMorada(p4, "Braga")
pessoa.mudancaMorada(p5, "Guarda")

print("\n=== Lista Final ====\n")

pessoa.toString(p1)
pessoa.toString(p2)
pessoa.toString(p3)
pessoa.toString(p4)
pessoa.toString(p5)

print("\n")
