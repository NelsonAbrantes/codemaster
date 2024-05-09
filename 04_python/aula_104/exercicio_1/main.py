from funcoes import *

dicionario = {
        "nome": "Nelson",
        "idade": "58",
        "morada": "Seia"
}

limpar()
print("\n")

print(f"Dicionário original: {dicionario}")
print("\n=== Dicionário com FOR ===\n")

for i in dicionario:
    print(f"{i}: {dicionario[i]}")

print("\n=== Dicionário apenas as chaves ===\n")

print(dicionario.keys())

print("\n=== Dicionário apenas as valores ===\n") 

print(dicionario.values())

print("\n")