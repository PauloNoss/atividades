segundos = int(input("Digite o valor em segundos: "))

# Calcular horas, minutos e segundos
horas = segundos // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos_restantes_finais = segundos_restantes % 60

# Imprimir o resultado
print(f"{segundos} segundos é igual a {horas} horas, {minutos} minutos e {segundos_restantes_finais} segundos.")
