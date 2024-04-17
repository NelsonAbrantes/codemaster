
print()

numero = int(input(" Digite um número de 1 a 100: "))

print()

if numero > 0:
    
    multiplo = 1

    while numero * multiplo <= 100:
        print(numero * multiplo)
        multiplo += 1
else:
    print("numero invalido.")        


print()