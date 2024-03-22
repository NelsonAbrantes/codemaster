print("\n")

original = "CodeMaster"
maiusculo = original.upper()
minusculo = original.lower()
capitalize = original.capitalize()

total_caracteres = len(original)
total_caracteres_2 = original.__len__()

caracteres_especifico = original.count("e")

substituir = original.replace("e", "X")


print("String 'original' = (" + original + ")\n")
print("String 'capitalizada' = (" + capitalize + ")")
print("String 'maiusculo' = (" + maiusculo + ")")
print("String 'minusculo' = (" + minusculo + ")\n")

print("String 'total de letras e' = (" + str(caracteres_especifico) + ")")
print("String 'tamanho total com método' = (" + str(total_caracteres_2) + ")")
print("String 'tamanho total com função' = (" + str(total_caracteres) + ")\n")

print("String 'substitui todo (e) por (X)' = (" + substituir + ")")
