nome_vendedor = input("Digite o nome do vendedor: ")
carros_vendidos = int(input("Digite o número de carros vendidos: "))
valor_vendas = float(input("Digite o valor total das vendas em reais: "))

salario_fixo = 500.00
comissao_por_carro = 50.00
comissao_valor_vendas = 0.05 * valor_vendas

salario_total = salario_fixo + (carros_vendidos * comissao_por_carro) + comissao_valor_vendas

# Imprimir o salário do vendedor
print(f"O salário do vendedor {nome_vendedor} é de R${salario_total:.2f}.")


