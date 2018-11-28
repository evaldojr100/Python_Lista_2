'''20) (BACKES, 2012) Dados três valores, A, B, C, verificar se eles podem ser valores dos lados
de um triângulo e, se forem, se e um triângulo escaleno, equilátero ou isóscele, considerando
os seguintes conceitos:
O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois
lados.
Chama-se equilátero o triângulo que tem três lados iguais.
Denominam-se isósceles o triángulo que tem o comprimento de dois lados iguais.
Recebe o nome de escaleno o triangulo que tem os três lados diferentes.
Salve o programa com o nome “​ 20_triangulo.py ​ ”.'''

l1=float(input("Digite o lado 1 do triangulo:"))
l2=float(input("Digite o lado 2 do triangulo:"))
l3=float(input("Digite o lado 3 do triangulo:"))

if l1<(l2+l3) and l2<(l1+l3) and l3<(l1+l2):
    if l1 == l2 == l3:
        print("Triangulo Equilatero!!!")
    elif l1 != l2 != l3:
        print("Triangulo Escaleno!!!")
    else:
        print("Triangulo Isósceles!!!")
else:
    print("Não é um Triangulo!!!")