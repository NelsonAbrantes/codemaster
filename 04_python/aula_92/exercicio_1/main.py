
print()

numero = int(input(" Digite um número para obter a sua tabuada de 0 a 10: "))

print()

if 0 <= numero <= 10:
    
    print(f" === tabuada do ( {numero} ) === \n")
    x = 0
    while x <= 10:
        print(f"{numero} X {x} = {numero * x}")
        x += 1
else:
    print("numero invalido.")

print()