nota_lab = float(input("Nota do trabalho de laboratório: "))
nota_sem = float(input("Nota da avaliação semestral: "))
nota_exame = float(input("Nota do exame final: "))

media = (nota_lab * 2 + nota_sem * 3 + nota_exame * 5) / 10

if 0 <= media < 3:
    print("Aluno reprovado.")
elif 3 <= media < 5:
    print("Aluno em recuperação.")
else:
    print("Aluno aprovado.")
