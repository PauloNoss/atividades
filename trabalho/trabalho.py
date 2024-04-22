nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura (em centímetros): "))
peso = float(input("Digite seu peso (em quilogramas): "))

imc = peso / (altura / 100) ** 2

if imc < 18.5:
    classificacao = "Abaixo do Peso"
elif 18.5 <= imc <= 24.9:
    classificacao = "Peso Ideal (Para Bens)"
elif 25.0 <= imc <= 29.9:
    classificacao = "Sobrepeso"
elif 30.0 <= imc <= 34.9:
    classificacao = "Obesidade Grau 1"
elif 35.0 <= imc <= 39.9:
    classificacao = "Obesidade Grau 2"
else:
    classificacao = "Obesidade Grau 3"

print(f"\nNome: {nome}")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")