hora_chegada = int(input("Hora de chegada (0-23): "))
min_chegada = int(input("Minuto de chegada (0-59): "))
hora_saida = int(input("Hora de saída (0-23): "))
min_saida = int(input("Minuto de saída (0-59): "))

tempo_total_min = (hora_saida * 60 + min_saida) - (hora_chegada * 60 + min_chegada)
tempo_total_horas = -(-tempo_total_min // 60)  # Arredonda para cima

if tempo_total_horas <= 2:
    preco = tempo_total_horas * 1
elif 3 <= tempo_total_horas <= 4:
    preco = tempo_total_horas * 1.4
else:
    preco = tempo_total_horas * 2

print(f"Preço cobrado pelo estacionamento: R$ {preco:.2f}")
