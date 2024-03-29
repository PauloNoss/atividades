salario_base = float(input("Digite o salário-base do funcionário: "))
salario_receber = salario_base * 1.05  # adição da gratificação de 5%
salario_receber -= salario_receber * 0.07  # subtração do imposto de 7%
print(f"O salário a receber é: R$ {salario_receber:.2f}")


