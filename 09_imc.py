'''9) (BACKES, 2012) Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua
classificação de acordo com a tabela abaixo:
IMC         Classificação
< 18,5      Abaixo do peso
18,6 -      24,9 Saudável
25,0 -      29,9 Peso em excesso
30,0 -      34,9 Obesidade grau I
35,0 -      39,9 Obesidade grau II
>= 40,0     Obesidade grau III'''

altura=float(input("Digite sua altura:"))
peso=(float(input("Digite seu peso:")))

imc= peso/altura**2

if imc <= 18.5:
    print("Abaixo do Peso")
elif 18.5 < imc < 24.9:
    print("Saudavel")
elif 25 <= imc <= 29.9:
    print("Peso em Excesso")
elif 30 < imc < 34.9:
    print("Obesidade grau I")
elif 35 < imc < 39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")
