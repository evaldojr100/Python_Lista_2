'''17) (BACKES, 2012) Leia a distância em Km e a quantidade de litros de gasolina consumidos
por um carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem de
acordo com a tabela abaixo:
Menor que 8 Venda o carro
Entre 8 e 14 Econômico
Maior que 14 Super econômico
Salve o programa com o nome “​ 17_consumo_gasolina'''

km=float(input("Digite a distancia em km:"))
litros=float(input("Digite quantos litros foram consumidos:"))

consumo=km/litros

if consumo < 8:
    print("venda o carro!!")
elif 8 < consumo <= 14:
    print("Econômico!!")
elif consumo > 14:
    print("Super Economico!!")

