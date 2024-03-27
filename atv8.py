#Calcule a média de um aluno na disciplina de ED. Para isso solicite o 
#nome do aluno, a nota da prova e a nota qualitativa. Sabe-se que a nota 
#da prova tem peso 2 e a nota qualitativa peso 1. Mostre a média como resultado.
nome_aluno=(input('digite seu nome:'))
av1=int(input('digite o valor da prova'))
av2=int(input('digite o valor da prova qualitativa'))
media_final=(av2+(av1*2))/3
print(f'o aluno {nome_aluno} tirou a media de {media_final}')