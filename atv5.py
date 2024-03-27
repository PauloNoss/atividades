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