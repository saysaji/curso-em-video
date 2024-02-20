frase= '  Curso em Vídeo Python  '
print (frase[:14])

print ('''Meu conselho é que se case. Se você arrumar uma boa esposa, será feliz; se arrumar uma esposa ruim, se tornará um filósofo.''')

print (frase.upper().count('O'))

print (len(frase.strip()))

frase= frase.replace('Python','é muito legal')
print (frase)

div= frase.split()
print (div[0][2])

nome= str(input('qual seu nome?').strip())
nomes= nome.split()
print ('Seu nome escrito em maiúsculo é:{}'.format(nome.upper()))
print ('Seu nome escrito em minúsculo é:{}'.format(nome.lower()))
print ('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
print ('Seu primeiro nome é {} e seu nome tem {} letras.'.format(nomes[0], len(nomes[0])))


num= int(input('digite um número:'))
u= num // 1 % 10
d= num // 10 % 10
c= num // 100 % 10
m= num // 1000 % 10
print ('unidade:{}'.format(u))
print ('dezena:{}'.format(d))
print ('centena:{}'.format(c))
print ('milhar:{}'.format(m))


cidade= str(input('qual cidade voce nasceu?')).strip()
print (cidade[:5].upper() == 'SANTO')


nomee= str(input('qual seu nome?')).strip()
print ('seu nome tem "silva"?', ('silva' in nomee.lower()))


frasee= str(input('digite uma frase:')).lower().strip()
print ('A letra "a" apareceu {} vezes na frase.'.format(frasee.count('a')))
print ('A primeira letra "a" aparece na {} posição.'.format(frasee.find('a')+1))
print ('A ultima letra "a" aparece na {} posição.'.format(frasee.rfind('a')+1))


nomeee= str(input('Qual seu nome?')).strip()
no= nomeee.split()
print ('Seu primeiro nome é {}'.format(no[0]))
print ('Seu ultimo nome é {}'.format(no[len(no)-1]))
