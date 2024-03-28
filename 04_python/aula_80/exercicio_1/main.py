
print("{:=20")

temperatura = float(input("Qual é a temperatura atual?"))
chover = input("Esta a chover?")

if(temperatura <= 18):
    print("vestir roupas grossas e casaco.")
elif(temperatura < 28):
    print("vestir roupas normais")
else:
    print("vestir roupas de praia")
if(chover.lower() == "sim"):
    print("levar chapéu-de-chuva")
print("ir passear")
