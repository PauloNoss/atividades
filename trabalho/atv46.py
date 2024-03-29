media_aprovacao = 7
nota_primeira_avaliacao = float(input("Digite a nota da primeira avaliação: "))

nota_segunda_avaliacao = (3 * media_aprovacao - nota_primeira_avaliacao) / 2
print(f"A nota necessária na segunda avaliação para alcançar a média mínima de aprovação é {nota_segunda_avaliacao:.2f}.")

