altura_degrau = float(input("Digite a altura do degrau da escada: "))
altura_desejada = float(input("Digite a altura que deseja alcançar subindo a escada: "))
degraus_a_subir = altura_desejada / altura_degrau
import math
degraus_a_subir = math.ceil(degraus_a_subir)
print(f"O usuário deverá subir {degraus_a_subir} degraus para atingir seu objetivo.")

