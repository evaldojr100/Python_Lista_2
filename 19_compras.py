'''19) (PUGA & RISSETI, 2016) Uma loja de departamentos está oferecendo diferentes formas de
pagamento, conforme as opções listadas a seguir. Faça um algoritmo que leia o valor total de
uma compra e calcule o valor do pagamento final de acordo com a opção escolhida. Se a
escolha for por pagamento parcelado, calcule também o valor da parcela. Ao final, apresente o
valor total e o valor das parcelas. Salve o programa com o nome “​ 19_compras.py ​ ”.
a) Pagamento à vista: conceder desconto de 5%.
b) Pagamento em 3 parcelas: o valor não sofre alteração.
c) Pagamento em 5 parcelas: acréscimo de 2%.
d) Pagamento em 10 parcelas: acréscimo de 8%.'''

valor=float(input("Digite o Valor da Compra:"))
print("Digite 1 para pagamento a vista")
print("Digite 2 para pagamento em 3 parcelas")
print("Digite 3 para pagamento em 5 parcelas")
print("Digite 4 para pagamento em 10 parcelas")
escolha=int(input("Sua escolha:"))

if escolha==1:
    print("Valor Total %.2f \n"%(valor-(valor*0.05)))
elif escolha==2:
    print("Valor Total %.2f \n Valor Parcelas: %d" % (valor , valor/3))
elif escolha == 3:
    valor+=valor*0.02
    print("Valor Total %.2f \n Valor Parcelas: %d" % (valor, valor / 5))
elif escolha == 4:
    valor += valor * 0.08
    print("Valor Total %.2f \n Valor Parcelas: %d" % (valor, valor / 10))
else:
    print("Escolha invalida!!")



