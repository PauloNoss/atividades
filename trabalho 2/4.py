num = float(input("Digite um número: "))

if num >= 0:
    quadrado = num ** 2
    raiz = num ** 0.5
    print(f"Quadrado: {quadrado}")
    print(f"Raiz quadrada: {raiz}")
else:
    print("Número inválido. O número deve ser positivo.")
