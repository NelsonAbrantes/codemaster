
print()
print(" === Maior e menor numeros ===\n")

total_numeros = int(input(" Digite o total de números que serão analisados: "))

maior = ""
menor = ""
loop = 1

print()

while(loop <= total_numeros):
    
    numero = int(input(f" Digite o ( {loop}º ) número: "))
    if loop == 1:
        maior = numero
        menor = numero  
    else:
        if numero > maior :
            maior = numero
        if numero < menor :
            menor = numero
    loop += 1

print()
print(f"--- O maior número digitado foi: ({maior}) ---")
print(f"--- O menor número digitado foi: ({menor}) ---\n")