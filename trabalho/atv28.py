importancia_total = 780000
porcentagem_primeiro = 0.46
porcentagem_segundo = 0.32
quantia_primeiro = importancia_total * porcentagem_primeiro
quantia_segundo = importancia_total * porcentagem_segundo
quantia_terceiro = importancia_total - quantia_primeiro - quantia_segundo
print(f"Quantia ganha pelo primeiro ganhador: R$ {quantia_primeiro:.2f}")
print(f"Quantia ganha pelo segundo ganhador: R$ {quantia_segundo:.2f}")
print(f"Quantia ganha pelo terceiro ganhador: R$ {quantia_terceiro:.2f}")

