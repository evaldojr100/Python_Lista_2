'''11) (Python.org.br) Faça um Programa que peça um número e informe se o número é inteiro ou
decimal. Salve o programa com o nome “​ 11_inteiro_ou_decimal.py ” ​ .'''

num=float(input("Digite um numero:"))


if num // 1 == num:
    print(num // 1)
    print("Inteiro")
else:
    print(num // 1)
    print("Decimal")
