from funcoes import *

limpar()

total = int(input(" Digite o total de eleitores: "))
validos = int(input(" Digite o total de votos validos: "))
brancos = int(input(" Digite o total de votos brancos: "))
nulos = int(input(" Digite o total de votos nulos: "))
nao_votaram = total - (validos + brancos + nulos)

limpar()

print(f"A percentagem de votos validos foi de ( {calcular_percentagem(total, validos):.1f}% )")
print(f"A percentagem de votos brancos foi de ( {calcular_percentagem(total, brancos):.1f}% )")
print(f"A percentagem de votos nulos foi de ( {calcular_percentagem(total, nulos):.1f}% )")
print(f"A percentagem de nao votantes foi de ( {calcular_percentagem(total, nao_votaram):.1f}% )")