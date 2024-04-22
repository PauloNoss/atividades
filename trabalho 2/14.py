def get_dia_semana(numero):
    dias = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    return dias.get(numero, "Número inválido")

numero_dia = int(input("Digite um número de 1 a 7: "))
print(get_dia_semana(numero_dia))
