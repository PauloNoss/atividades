hora_inicio = int(input("Digite a hora de início (0-23): "))
minuto_inicio = int(input("Digite o minuto de início (0-59): "))
segundo_inicio = int(input("Digite o segundo de início (0-59): "))
duracao_segundos = int(input("Digite a duração em segundos: "))
segundos_totais_inicio = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio
segundos_totais_termino = segundos_totais_inicio + duracao_segundos
hora_termino = segundos_totais_termino // 3600 % 24
minuto_termino = segundos_totais_termino // 60 % 60
segundo_termino = segundos_totais_termino % 60
print(f"O novo horário do término da experiência é: {hora_termino} horas, {minuto_termino} minutos, {segundo_termino} segundos.")


