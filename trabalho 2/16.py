base_maior = float(input("Digite o valor da base maior do trapézio: "))
base_menor = float(input("Digite o valor da base menor do trapézio: "))
altura = float(input("Digite o valor da altura do trapézio: "))

if base_maior > 0 and base_menor > 0:
    area = ((base_maior + base_menor) * altura) / 2
    print(f"A área do trapézio é: {area}")
else:
    print("Os valores da base maior e base menor devem ser maiores que zero.")
