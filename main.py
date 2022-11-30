# Implementar uma solução, em Python, que resolva a seguinte questão; calcular o valor de uma
#compra, sendo que o preço unitário é R$ 10,00
#Se for feita uma compra de até 10 unidades, não há desconto.
#Para compras entre 11 e 20 unidades é dado um desconto de 10%
#Acima de 20 unidades, é dado um desconto de 20%

produto=eval(input('O preço do produto é R$10,00, a unidade, digite a quantidade desejada: '))
total=(produto*10)
if(produto<=10):
    resultado=(f'Seu produto deu um total de R${total},sem desconto')
elif(produto>10<=20):
    resultado = (f'Seu produto deu um total de R${(total*0.9):.2f},com 10% de desconto!')
if(produto>20):
    resultado = (f'Seu produto deu um total de R${(total * 0.8):.2f},com 20% de desconto!')
print(resultado)