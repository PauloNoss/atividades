nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))

media = (nota1 * 1 + nota2 * 2) / 3

if media >= 70:
    print(f"Média: {media:.2f}. Aluno aprovado.")
else:
    print(f"Média: {media:.2f}. Aluno reprovado.")
