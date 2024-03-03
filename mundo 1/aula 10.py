import random
n1= random.randint(1,5)
n2= int(input('Escolha um número entre 1 e 5:'))
print (f'voce acertou!'if n2 == n1 else'voce errou :( o número certo era:{}'.format(n1))


vlo= float(input('qual a velocidade que voce esta dirigindo?'))
multa= (vlo-80)*7
print (f'velocidade normal'if vlo <=80 else'multado! reduza a velocidade, voce foi multado em R${:.2f}'.format(multa))


nu= int(input('digite um número:'))
resultado= nu % 2
print (f'Seu número é PAR'if resultado == 0 else 'Seu número é íMPAR')


km= float(input('quantos km tem a sua viangem?'))
preço=km * 0.50 if km <=200 else km * 0.45
print ('O preço dessa viagem é de R${:.2f}'.format(preço))


ano= int(input('Qual ano voce quer analisar?:'))
bioun= ano % 4 ==0 and ano % 100 == 0 or ano % 400 ==0 
print('seu ano é bissexto'if bioun == 0 else 'seu ano não é bissexto')