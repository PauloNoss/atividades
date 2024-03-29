comprimento_terreno = float(input("Digite o comprimento do terreno em metros: "))
largura_terreno = float(input("Digite a largura do terreno em metros: "))
preco_metro_tela = float(input("Digite o preço do metro de tela em reais: "))

perimetro_terreno = 2 * (comprimento_terreno + largura_terreno)
custo_cerca = perimetro_terreno * preco_metro_tela
