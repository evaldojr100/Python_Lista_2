'''7) (BACKES, 2012) Faça um algoritmo que calcule a média ponderada das notas de 3 provas.
A primeira e a segunda prova tem peso 1 e a terceira tem peso 2. Ao final, mostrar a média do
aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou
superior a 60 pontos. Salve o programa com o nome “​ 07_media_ponderada.py ​ ”.'''

n1=float(input("Digite a primeira nota:"))
n2=float(input("Digite a segunda nota:"))
n3=float(input("Digite a terceira nota:"))

media=(n1+n2+(n3*2))/(1+1+2)

if media>=60:
    print("Aprovado")
else:
    print("Reprovado")