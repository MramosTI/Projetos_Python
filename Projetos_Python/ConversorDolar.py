from time import sleep
print('¨'*50)
print('\033[0;32;1mCONVERSOR DE DÓLAR PARA REAL...\033[m')
print('¨'*50)
real = float(input('Quantos reais você quer converter? R$'))
dolar = float(input('Qual a cotação do dólar atual? U$'))
conversao = real / dolar
print('\033[0;31;1mCONVERTENDO...\033[m')
sleep(2)
print('Convertendo \033[0;32;1mR${:.2f}\033[m reias você terá \033[0;32;1mU${:.2f}\033[m em dólar. '.format(real, conversao))