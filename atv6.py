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