#import functions
from functions import *
print("\n")

test()
calculadobro()

def testar(numero):
    resultado = numero * 2
    print(f"O doubro do numero ({numero}) é ({resultado}).\n")

testar(2)
testar(8)

x = 99
testar(x)

y = float(input(" digite o numero: "))
testar(y)

testar(float(input(" digite o numero: ")))
