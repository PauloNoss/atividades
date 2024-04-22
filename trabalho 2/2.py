num = float(input("Digite um número: "))

if num >= 0:
    raiz = num ** 0.5
    print(f"A raiz quadrada de {num} é {raiz}.")
else:
    print("Número inválido. Não é possível calcular a raiz de um número negativo.")
