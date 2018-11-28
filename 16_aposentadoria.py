'''16) (BACKES, 2012) Leia a idade e o tempo de serviço de um trabalhador e escreva se ele
pode ou não se aposentar. As condições para aposentadoria são:
Ter pelo menos 65 anos,
Ou ter trabalhado pelo menos 30 anos,
Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
Salve o programa com o nome “​ 16_aposentadoria.py ” ​ .'''

idade = int(input("Digite a idade:"))
tempo = int(input("Digite o tempo de serviço do trabalhador:"))

if idade >= 65 or tempo >= 30 or 60 <= idade < 65 and 25 <= tempo < 30:
    print("Pode se aposentar!!!")
else:
    print("Não pode se aposentar")


