#trabalho de progamação
#pergunta 1
print('Calcule a média de quatro números inteiros dados.')
numero1=int(input('digite o 1º numero:')) 
numero2=int(input('digite um 2º numero:'))
numero3=int(input('digite um 3º numero:')) 
numero4=int(input('digite um 4º numero:')) 
resultado= (numero1 + numero2 + numero3 + numero4) /4
print('a media é',resultado )
#pergunta 2
#Leia uma temperatura dada na escala Celsius (C) e imprima o equivalente em Fahrenheit (F). (Fórmula de conversão: F = 9/5 * C + 32)
temperatura= int(input('digite a tempera em cº:'))
formula= 9/5* temperatura +(32)
#pergunta 3
#Leia uma quantidade de chuva dada em polegadas e imprima o equivalente em milímetros (25,4 mm = 1 polegada)
polegada=int(input('digite quantidade de chuva em polegada'))
calculo=polegada*25.4
print(f'choveu {calculo} milímetros de chuva')
print('a temperatura e fahrenheith é de:',formula )
#pergunta 4
#Calcule o quadrado de um número, ou seja, o produto de um número por si mesmo.
numero=int(input('digite o numero que vai ser elevado ao quadrado'))
calculo= numero*numero
print('o resultado é:',calculo)
#pergunta 5 O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos, ambos aplicados ao 
#custo de fábrica. Supondo que a porcentagem do distribuidor seja de 
#12% e a dos impostos de 45%, prepare um algoritmo para ler o custo de 
#fábrica do carro e imprimir o custo ao
#consumidor
custovei=int(input('digite o custo de fabrica do veiculo'))
formula=custovei*0.12
custoimp=custovei*0.45
valorfinal= custovei + formula + custoimp
print('o valor a ser vendido o veiculo é de ',valorfinal)
#O cardápio de uma lanchonete é dado abaixo. Prepare um algoritmo que 
#leia a quantidade de cada item que você consumiu e calcule a conta final
#a. Hambúrguer................. R$ 3,00
#b. Cheeseburger.............. R$ 2,50
#c. Fritas............................ R$ 2,50
#d. Refrigerante ................. R$ 1,00
#e. Milkshake..................... R$ 3,0
QH=int(input('quantos hamburguer foram consumidos?:'))
QF=int(input('quantas fritas foram consumidas?:'))
QC=int(input('quantos Cheeseburger foram consumidos?:'))
QR=int(input('quantos refrigerantes foram consumidos?:'))
QM=int(input('quantos milkshake foram consumidos?:'))
t=(QH*3)+(QC*2.50)+(QF*2.50)+(QR*1)+(QM*3)
print('valor total a pagar é de ',t)
#Uma companhia de carros paga a seus empregados um salário de R$ 
#500,00 por mês mais uma comissão de R$ 50,00 para cada carro 
#vendido e mais 5% do valor da venda. Elabore um algoritmo para 
#calcular e imprimir o salário do vendedor num dado mês recebendo 
#como dados de entrada o nome do vendedor, o número de carros
#vendidos e o valor total das vendas
nome_funcionario=input('digite o seu nome:')
NC=int(input('numero de carros vendidos'))
vtv=int(input('digite o valor total de vendas'))
vlr_carros=NC*50
vlr_vendas=vtv*0.05
t= vlr_carros + vlr_vendas +500
print(f'{nome_funcionario}vai receber o valor de {t}')
#Calcule a média de um aluno na disciplina de ED. Para isso solicite o 
#nome do aluno, a nota da prova e a nota qualitativa. Sabe-se que a nota 
#da prova tem peso 2 e a nota qualitativa peso 1. Mostre a média como resultado.
nome_aluno=(input('digite seu nome:'))
av1=int(input('digite o valor da prova'))
av2=int(input('digite o valor da prova qualitativa'))
media_final=(av2+(av1*2))/3
print(f'o aluno {nome_aluno} tirou a media de {media_final}')
#Sabendo que a média de aprovação é 7, e a formula para cálculo da 
#média consiste em a primeira avaliação com peso 1 e a segunda 
#avaliação com peso 2, sendo divido por 3, realize o cálculo de quanto 
#deve ser a nota da segunda avaliação para que o resultado seja a
nota1=int(input('insira a nota 1:'))
nota2=((7*3)-nota1)/2
print(f'você precisa de {nota2}para ser aprovado')
#Sabendo que a média de aprovação é 7, e a formula para cálculo da 
#média consiste em a primeira avaliação com peso 1 e a segunda 
#avaliação com peso 2, sendo divido por 3, realize o cálculo de quanto 
#deve ser a nota da primeira avaliação para que o resultado seja a 
#aprovação. Elabore a fórmula para o cálculo e a representação do 
#algoritmo para o mesmo
not2 = int(input("Digite a nota da segunda avaliação: "))
not1 = (7 * 3 - not2 * 2) / 1
print("A nota necessária na primeira avaliação para alcançar a média é:", not1)