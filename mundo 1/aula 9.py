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
u= num // 1 &10
d= num // 10 & 10
c= num // 100 & 10
m= num // 1000 & 10
print ('unidade:{}'.format(u))
print ('dezena:{}'.format(d))
print ('centena:{}'.format(c))
print ('milhar:{}'.format(m))