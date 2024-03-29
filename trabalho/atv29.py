dias_trabalhados = int(input("Digite o número de dias trabalhados pelo encanador: "))

pagamento_por_dia = 30.00
desconto_previdencia = 0.11
desconto_imposto_renda = 0.08
quantia_bruta = dias_trabalhados * pagamento_por_dia
desconto_total = quantia_bruta * (desconto_previdencia + desconto_imposto_renda)
quantia_liquida = quantia_bruta - desconto_total
print(f"A quantia líquida a ser paga é: R$ {quantia_liquida:.2f}")


