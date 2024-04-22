numero = int(input("Digite um número inteiro maior que zero: "))

if numero <= 0:
    print("Número inválido.")
else:
    soma = sum(int(digito) for digito in str(numero))
    print(f"A soma dos algarismos é: {soma}")
