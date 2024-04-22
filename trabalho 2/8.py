nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    media = (nota1 + nota2) / 2
    print(f"A média das notas é: {media}")
else:
    print("Notas inválidas. As notas devem estar entre 0 e 10.")
