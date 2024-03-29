g1 = float(input("Digite a nota de G1: "))
g2 = float(input("Digite a nota de G2: "))
media_semestre = (g1 + (g2 * 2)) / 3
if media_semestre >= 7.0:
    print("Parabéns! Você foi aprovado.")
else:
    print(f"Sua média do semestre é: {media_semestre}. Infelizmente, você não atingiu a nota mínima para aprovação.")

