#Sabendo que a média de aprovação é 7, e a formula para cálculo da 
#média consiste em a primeira avaliação com peso 1 e a segunda 
#avaliação com peso 2, sendo divido por 3, realize o cálculo de quanto 
#deve ser a nota da primeira avaliação para que o resultado seja a 
#aprovação. Elabore a fórmula para o cálculo e a representação do 
#algoritmo para o mesmo
not2 = int(input("Digite a nota da segunda avaliação: "))
not1 = (7 * 3 - not2 * 2) / 1
print("A nota necessária na primeira avaliação para alcançar a média é:", not1)