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