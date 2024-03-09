from datetime import date
casa= float(input('Qual o valor da casa?'))
salario= float(input('Qual o salario do comprador?'))
anos= int(input('Em quantos anos pretende comprar?'))
prestação= casa/(anos*12)
minimo= salario * 30 / 100
print ('para compra essa casa de R${:.2f} com o salario de R${:.2f} em {}anos voce precisara de R${:.2f} de pestação.'.format(casa,salario,anos,prestação))
if prestação <=minimo:
    print('imprestimo aceito')
else:
    print('imprestimo negado')

numero= int(input('didite um número:'))
print('''escolha uma da opções:
[1] comverter para binário
[2] converter para octal 
[3] converter para hexadecimal''')
opção= int(input('escolha uma das opções:'))
if opção==1:
    print('seu número para binário é: {}'.format(bin(numero)[2:]))
elif opção==2:
    print('seu número para octal é: {}'.format(oct(numero)[2:]))
elif opção==3:
    print('seu número para hexadecimal é: {}'.format(hex(numero)[2:]))
else:
    print('opção inválida!!!')

num1= int(input('digite um número: '))
num2= int(input('digite um segundo número: '))
if num1> num2:
    print('O primeiro número é maior')
elif num2> num1:
    print('o segundo número é maior')
else:
    print('seus números tem o mesmo valor')

nasc= int(input('qual sua data de nascemento?: '))
idade= 2024- nasc
if idade == 18:
    print('voce precisa se alistar imediatamente!')
elif idade > 18:
    saldo = idade - 18
    print('voce deveria se alistar faz {} anos'.format(saldo))
else:
    saldo= 18 - idade
    print('ainda falta {} anos para voce se alistar'.format(saldo))



nota1= float(input('primeira nota do aluno: '))
nota2= float(input('segunda nota do aluno: '))
nota3= float(input('terceira nota do aluno: '))
media= (nota1+nota2+nota3)/3
if media>=7:
    print('parabens voce passou! sua nota foi {:.1f}.'.format(media))
elif media<5:
    print('reprovado!sua nota foi {:.1f} tente denovo no proximo ano.'.format(media))
elif media >=5 and 7:
    falta= 7 - media
    print('recuperação! sua nota foi {:.1f} voce precisa de {:.1f} para passar.'.format(media,falta))
else:
    print('erro na informações!')