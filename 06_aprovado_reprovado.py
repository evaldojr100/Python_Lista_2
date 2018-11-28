'''6) Escreva um algoritmo que leia 2 notas de um aluno do IFRO e informe se o mesmo está
aprovado ou reprovado na disciplina, considerando que para aprovação a nota tem que ser
maior ou igual a 6. Salve o programa com o nome “​ 06_aprovado_reprovado.py ​ ”.'''

n1=float(input("Digite a primeira nota:"))
n2=float(input("Digite a segunda nota:"))

if (n1+n2)/2>=6:
    print("Aprovado")
else:
    print("Reprovado")