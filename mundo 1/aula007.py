nom= input('qual seu nome?')
print ('olá {:20} como voce vai?'.format (nom))
print ('olá {:<20} como voce vai?'.format (nom))
print ('olá {:>20} como voce vai?'.format (nom))
print ('olá {:^20} como voce vai?'.format(nom))
print ('olá {:_>20} como voce vai?'.format(nom))
print ('olá {:_^20} como voce vai?'.format(nom))


n1= int(input('digite um falor:'))
n2= int(input('digite outro valor'))
print ('O resultado da divisão é igual a: {:.5f}'.format(n1/n2))


n1= int(input('fale um valor:'))
n2= int(input('fele outro valor:'))
s= n1+n2
su= n1-n2
div= n1/n2
divint= n1//n2
rdiv= n1%n2
pot= n1**n2
print (f'O resultado da soma desses valores é igual a: {format(s)}\nA subritração desses valores é: {format(su)}')
print ('divisão desses valores é: {:.3f}'.format(div), end= ', a')
print (f'divisãso inteira é: {format(divint)} e o resto da divisão é: {format(rdiv)}')
print (f'E por fim o resultado do valor {format(n1)} elevado a {format(n2)} potencia é igual a: {format(pot)}')