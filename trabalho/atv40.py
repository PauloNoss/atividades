investimento_amigo1 = float(input("Digite o valor investido pelo amigo 1: "))
investimento_amigo2 = float(input("Digite o valor investido pelo amigo 2: "))
investimento_amigo3 = float(input("Digite o valor investido pelo amigo 3: "))
valor_premio = float(input("Digite o valor total do prêmio: "))

total_investido = investimento_amigo1 + investimento_amigo2 + investimento_amigo3

parte_amigo1 = (investimento_amigo1 / total_investido) * valor_premio
parte_amigo2 = (investimento_amigo2 / total_investido) * valor_premio
parte_amigo3 = (investimento_amigo3 / total_investido) * valor_premio

# Imprimir a divisão do prêmio
print(f"Se ganharem, o amigo 1 ganharia R${parte_amigo1:.2f}, o amigo 2 ganharia R${parte_amigo2:.2f}, e o amigo 3 ganharia R${parte_amigo3:.2f}.")


