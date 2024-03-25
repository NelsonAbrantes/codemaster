

nome_1 = "Nelson"
nome2 = "Ana"
nome3 = "Sara"

idade = 19
morada = "Ariswil"


print("\n")
print("Nome: {:*20} x".format(nome_1))
print("Nome: {:<20} x".format(nome2))
print("Nome: {:<20} x".format(nome3))

print("Nome: {:#20} x".format(nome_1))
print("Nome: {:>20} x".format(nome2))
print("Nome: {:>20} x".format(nome3))

print("Nome: {:<20} x".format(nome_1))
print("Nome: {:^20} x".format(nome2))
print("Nome: {:^20} x".format(nome3))