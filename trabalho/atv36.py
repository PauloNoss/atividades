numero = int(input("Digite um número inteiro de 4 dígitos (de 1000 a 9999): "))

# Imprimir cada dígito em uma linha
print(numero // 1000)  # Milhares
print((numero % 1000) // 100)  # Centenas
print((numero % 100) // 10)  # Dezenas
print(numero % 10)  # Unidades


