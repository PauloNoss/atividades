valor_total = float(input("Digite o valor total da venda: "))
total_com_desconto = valor_total * 0.9
valor_parcela = valor_total / 3
comissao_a_vista = total_com_desconto * 0.05
comissao_parcelada = valor_total * 0.05
print(f"Total a pagar com desconto de 10%: R$ {total_com_desconto:.2f}")
print(f"Valor de cada parcela (3x sem juros): R$ {valor_parcela:.2f}")
print(f"Comissão do vendedor (venda à vista): R$ {comissao_a_vista:.2f}")
print(f"Comissão do vendedor (venda parcelada): R$ {comissao_parcelada:.2f}")



