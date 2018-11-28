'''8) (BACKES, 2012) O custo ao consumidor de um carro novo é a soma do custo de fábrica, da
comissão do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o
custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao
consumidor.
Até R$ 12.000,00 5% isento
Entre R$ 12.000,00 e R$ 25.000,00 10% 15
Acima de R$ 25.000,00 15% 20
Salve o programa com o nome “​ 08_custo_carro'''

custo=float(input("Digite o custo de fabrica: R$"))

if custo <= 12000:
    total = custo+(0.05*custo)
    print("Total R$",total)
elif 1200<custo <= 25000:
    total = custo+(0.1*custo)+(0.15*custo)
    print("Total R$", total)
elif custo > 25000:
    total = custo+(0.15*custo)+(0.2*custo)
    print("Total R$", total)