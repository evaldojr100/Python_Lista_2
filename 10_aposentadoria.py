'''10) Escreva um algoritmo que leia a idade e o sexo de um trabalhador informados pelo usuário
e, em seguida, caso o sexo seja feminino e sua idade seja maior ou igual a 60 anos ou sua
idade seja maior ou igual a 65 anos, informe que o(a) trabalhador está em condições de se
aposentar. Salve o programa com o nome “​ 10_aposentadoria ​ .py”.'''

idade=int(input("Digite a idade do trabalhador:"))
sexo=input("Digite o sexo (M/F):")

if (sexo=='f' and idade>=60) or idade>=65:
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")

