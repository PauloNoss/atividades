numero = int(input("Digite um número inteiro de três dígitos (de 100 a 999): "))
digito_centenas = numero // 100
digito_dezenas = (numero % 100) // 10
digito_unidades = numero % 10
numero_invertido = digito_unidades * 100 + digito_dezenas * 10 + digito_centenas

print(f"O número invertido é: {numero_invertido}")



