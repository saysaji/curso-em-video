n1= int(input('digite um número'))
print (f'analisando o primeiro valor {format(n1)}, seu antecessor é {format(n1-1)} e seu sucessor é {format(n1+1)}.')

n2= int(input('digite um número:'))
print (f'o dobro do valor {format(n2)} é: {format(n2*2)}\n O triplo desse valoré ilga a: {format(n2*3)}')
print ('A raiz quadrada desse vlor é igual a: {:.2f}'.format(n2**(1/2)))

n3= float(input('primeira nota do aluno:'))
n4= float(input('segunda nota do aluno:'))
nf= ((n3+n4)/2)
print (f'A media entre {format(n3)} e {format(n4)} é igual a: {format(nf)}.')

d= float(input('uma distancia em metros:'))
km= d/1000
hm= d/100
dam= d/10
dm= d*10
cm= d*100
mm= d*1000
print (f'a medida {format(d)}m corresponde a:\n{format(km)}km\n{format(hm)}hm\n{format(dm)}dm')
print (f'{format(cm)}cm\n{format(mm)}mm')
