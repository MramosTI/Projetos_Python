print('__'*50)
print('CALCULADORA DE DESCONTOS: ')
print('__'*50)
valor = float(input('Digite o valor a ser aplicado o desconto: R$'))
desconto = int(input('Digite o valor do desconto: % '))
vdesconto = valor - (valor * desconto)/100 
print('Com o desconto de %{} o valor de R${:.2f} passa para R${:.2f}'.format(desconto, valor, vdesconto))
