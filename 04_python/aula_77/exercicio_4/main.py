

nome_1 = "Nelson"
nome_2 = "Ana"
nome_3 = "Sara"



print("\n")
print("Nome: {:.*20} x".format(nome_1))
print("Nome: {:.<20} x".format(nome_2))
print("Nome: {:.<20} x".format(nome_3))

print("Nome: {:.#20} x".format(nome_1))
print("Nome: {:.>20} x".format(nome_2))
print("Nome: {:.>20} x".format(nome_3))

print("Nome: {:.<20} x".format(nome_1))
print("Nome: {:.^20} x".format(nome_2))
print("Nome: {:.^20} x".format(nome_3))

print("*" * 20)

saldo_1 = 12.00
saldo_2 = 34.00
saldo_3 = 123.00

print("{:.2f} | {:.2f} | {:.2f}".format(saldo_1+ saldo_2 + saldo_3))
