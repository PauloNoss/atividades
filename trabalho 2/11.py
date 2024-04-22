import math

num = float(input("Digite um número: "))

if num < 0:
    print("Número inválido.")
else:
    logaritmo = math.log(num)
    print(f"O logaritmo do número é: {logaritmo}")
