import functions

print()

c = float(input(" digite uma temperatura em celsius: "))
conversao = input("Voce deseja converter para (k)elvin ou (F)ahrenheit? ")

print(c)
print()
print(conversao)

if (conversao == "F"):
    functions.fahrenheit(c)
elif (conversao == "K"):
    functions.kelvin(c)
else:
    print("Erro!\n")

