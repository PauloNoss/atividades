valor = float(input("Digite o valor do produto: "))
estado = input("Digite o estado destino (MG, SP, RJ, MS): ")

impostos = {'MG': 0.07, 'SP': 0.12, 'RJ': 0.15, 'MS': 0.08}

if estado in impostos:
    preco_final = valor * (1 + impostos[estado])
    print(f"O preço final do produto no estado {estado} é: R$ {preco_final:.2f}")
else:
    print("Estado inválido.")
