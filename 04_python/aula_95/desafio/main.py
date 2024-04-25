
print()
print("==== Gerador de numeros inteiros ====\n")

inicio = int(input(" Digite o valor inicial da sua lista numérica: "))
fim = int(input(" Digite o valor final da sua lista numérica: "))
repeticoes = int(input(" Quantas vezes deseja exibir esta lista numérica: "))

repetir = None

for repetir in range(repeticoes):
    for i in range(inicio, fim + 1):
        print(i)
    print("--------")        