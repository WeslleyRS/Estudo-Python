usuario = input ('Digite seu úsuario: ')

print ('Seja bem-vindo(a) ao sistema de conversão BR/USD')

moeda = (input ('Você vai converter BRL Digite (BRL) Se for USD Digite (0): '))
if moeda == ('BRL'):
    dollar = float (input('Digite o valor atual do USD: '))
    real_contia = float (input('Digite o valor que você possui em BRL para conversão: '))
    real = 1
    conversao_brl = real_contia / dollar
    print (f'O valor que você possui em BRL é de R${real_contia} e o valor atual do dollar que voce inseriu é de ${dollar} fazendo a conversão você terá ${conversao_brl} cada BRL equivale a ${conversao_brl} USD')
else:
    usd = float (input('Digite o valor que você possui em USD: '))
    usd_valor = float(input('Digite o valor do USD: '))
    conversao_usd = usd * usd_valor
    equivalente_usd = (input(f'Cada Dolar equivale a R${usd_valor} '))
    print (f'Você possui ${usd} o valor que você inseriu do USD é de ${usd_valor} então você tera R${conversao_usd} BRL')
