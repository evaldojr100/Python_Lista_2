'''4) (Python.org.br) Faça um Programa que leia 2 números e em seguida pergunte ao usuário
qual operação ele deseja realizar, sendo possível somar, subtrair, dividir ou multiplicar. O
resultado da operação deve ser acompanhado de uma frase que diga se o número é:
● par ou ímpar;
● positivo ou negativo;
● inteiro ou decimal.
Salve o programa com o nome “​ 04_operacoes_com_numeros.py ​ ”.'''

num1=int(input("Digite o 1 numero:"))
num2=int(input("Digite o 2 numero:"))

opcao= input("Escolha a operação:\n(+) para adição\n(-) para subtração\n(*) para Multiplicação\n(/) para Divisão\nsua escolha:")

if opcao=='+' or opcao=='-' or opcao=='*' or opcao=='/':
    if opcao=='+':
        soma=num1 + num2
        print("\nResultado:",soma,"\n")

    elif opcao == '-':
        soma = num1 - num2
        print("\nResultado:", soma, "\n")

    elif opcao == '*':
        soma = num1 * num2
        print("\nResultado:", soma, "\n")

    elif opcao == '/':
        soma = num1 / num2
        print("\nResultado:", soma, "\n")


    if soma%2 == 0:
        print(soma,"é par")
    else:
        print(soma, "é impar")

    if soma > 0:
        print(soma, "é positivo")
    elif soma == 0:
        print(soma, "é zero")
    else:
        print(soma, "é negativo")

    if type(soma) == float:
        print(soma,"é decimal")
    else:
        print(soma, "é inteiro")
else:
    print("Opção invalida")