custo_fabrica = float(input("Digite o custo de fábrica do carro em reais: "))
porcentagem_distribuidor = 12 / 100
porcentagem_impostos = 45 / 100

custo_consumidor = custo_fabrica + (custo_fabrica * porcentagem_distribuidor) + (custo_fabrica * porcentagem_impostos)

# Imprimir o custo ao consumidor
print(f"O custo ao consumidor do carro é de R${custo_consumidor:.2f}.")
