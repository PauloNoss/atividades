print("Cardápio:")
print("a. Hambúrguer................. R$ 3,00")
print("b. Cheeseburger.............. R$ 2,50")
print("c. Fritas............................ R$ 2,50")
print("d. Refrigerante ................. R$ 1,00")
print("e. Milkshake..................... R$ 3,00")

quantidade_hamburguer = int(input("Digite a quantidade de hambúrgueres consumidos: "))
quantidade_cheeseburger = int(input("Digite a quantidade de cheeseburgers consumidos: "))
quantidade_fritas = int(input("Digite a quantidade de porções de fritas consumidas: "))
quantidade_refrigerante = int(input("Digite a quantidade de refrigerantes consumidos: "))
quantidade_milkshake = int(input("Digite a quantidade de milkshakes consumidos: "))

total_conta = (3.00 * quantidade_hamburguer) + (2.50 * quantidade_cheeseburger) + (2.50 * quantidade_fritas) + (1.00 * quantidade_refrigerante) + (3.00 * quantidade_milkshake)

print(f"A conta final é de R${total_conta:.2f}.")
