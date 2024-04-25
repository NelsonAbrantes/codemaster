
print()
print(" === Contaqbilizador de numeros ===\n")

total_numero = int(input(" Digite o total de números que serão analisados: "))
pares = 0
impares = 0
numeros = 1

print()

while(numeros <= total_numero):

    numero = int(input(f" Digite o {numeros}º número: "))
    if(numero % 2 == 0):
        pares += 1
    else:
        impares += 1    
    numeros += 1

print()
print(f"--- Total de números PARES: ({pares}) ---")
print(f"--- Total de números IMPARES: ({impares}) ---\n")
