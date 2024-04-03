print()

print("INICIO")

pergunta_1 = float(input("Tens carro?"))

if(pergunta_1.lower() == "sim"):
    pergunta_2 = input(" Qual é a cor? ")
    if(pergunta_2.lower() == "vermelho"):
        print("vai a festa.")
    elif(pergunta_2.lower() == "verde"):
        print("vai acampar")
        pergunta_3 = input(" está a chover?")
        if(pergunta_3.lower() == "sim"):
            print("Levas chapeu de chuva.")
        else:
            print("Levas oculos de sol.")
    else:
        print("vai a praia.")
else:
    pergunta_4 = input(" Tens uma mota?")
    if(pergunta_4.lower() == "sim"):
        print("Usa a tua mota")
    else:
        print("usa a tua bike.")
