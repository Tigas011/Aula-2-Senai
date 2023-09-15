# 1 - Crie uma condição para comparar idades: 45 e 18 -  QUAL É MENOR E QUAL É MAIOR?
idade1 = 45
idade2 = 18
if idade1 > idade2:
    maior = idade1
    menor = idade2
 else:
     maior = idade2
     menor = idade1
 print("Idade maior:", maior, "(ta quase aposentando em)")
 print("Idade menor:", menor, "(ta na flor da pele meu jovem)")


# 2 - Crie um sistema para permitir a verificação de menores em um show
 idade = int(input("Digite sua idade "))
 if idade < 18:
     print("Tá de menor ainda rapaz, volte para casa!")

# 3 - Crie um algoritmo que permita a entrada de 3 notas de alunos, utilize o bloco de código if() para verificar se o aluno passou.
nota1 = int(input("Digite a nota do primeiro aluno "))
if(nota1 >= 7):
    print("Parabens, você foi aprovado!")
else:
    print("Reprovado! se esforce mais da próxima vez")

nota2 = int(input("Digite a nota do segundo aluno "))
if(nota2 >= 7):
    print("Parabens, você foi aprovado!")
else:
    print("Reprovado! se esforce mais da próxima vez")

    nota3 = int(input("Digite a nota do terceiro aluno "))
if(nota3 >= 7):
    print("Parabens, você foi aprovado!")
else:
    print("Reprovado! se esforce mais da próxima vez")
