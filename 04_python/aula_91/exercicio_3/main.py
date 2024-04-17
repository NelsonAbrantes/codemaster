print()

pergunta = input(" Desejas Tirar a carta de condução? ")
resposta = ""
teste = 1


if( pergunta.lower() == "sim"):
    input("Voce passou no teste? ")
    while (resposta.lower() != "sim"):
        print()
        print(f"estudar para o teste numero {teste}.")
        resposta = input(f" Voce passou no {teste}º teste?\n")
        teste += 1    
    print(" Parabéns!")    
else:
    print(" Usa os transportes publicos.")

print()    
