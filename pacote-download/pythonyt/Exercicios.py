"""
1- Crie um programa que escreva "Olá Mundo!" na tela
print('Olá, Mundo!')

========================================================================================================================

2- Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas
nome = input('Informe seu nome: ')
print(f'Seja bem vindo {nome}!')

========================================================================================================================

3- Crie um programa que leia dois números e mostre a soma entre eles
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print(n1+n2)

========================================================================================================================

5- Faça um programa que leia um número inteiro e mostre na tela o seu sucessos e o seu antecessor
num = int(input('Digite um número: '))
ant = num - 1
suc = num + 1
print('O sucessor do número {} é {} e o antecessor é {}'.format(num, suc, ant))

========================================================================================================================

6- Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada
num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('O dobro do numéro {} é {}, o triplo é {} e a raiz quadrada é {}'.format(num, dobro, triplo, raiz))

========================================================================================================================

7- Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2) / 2
print('A média das notas {} e {} é: {}'.format(n1, n2, media))

========================================================================================================================

8- Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros
valor = int(input('Digite um valor em metros: '))
cm = valor * 100
ml = valor * 1000
print('O valor {} em centímetros é {} e em milímetros é {}'.format(valor, cm, ml))

========================================================================================================================

9- Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
valor = int(input('Digite um número inteiro: '))
contador = 0

while(contador <= 10):
    print('{} x {} = {}'.format(contador, valor, (contador*valor)))
    contador = contador + 1

========================================================================================================================

10- Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
($1,00 = R$3,27)
real = float(input('Informe quantos reais (R$) você possui: R$ '))
conv = real / 3.27
print('Com os R${} que você possui, você pode comprar ${}'.format(real, conv))

========================================================================================================================

11- Faça um programa que leia a largura e a altura de uma parede em emtros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
alt = int(input('Digite a altura da parece: '))
lar = int(input('Digite a largura da parede: '))
area = alt * lar

if area <= 2.0:
    print('A área da parede é de {}m² e será necessária 1 litro de tinta'.format(area))
else:
    litro = area // 2
    print('A área da parede é de {}m² e serão necessárias {} litros de tintas'.format(area, litro))

========================================================================================================================

12- Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
valor = int(input('Digite o preço do produto: R$ '))
desc = valor * 0.05
vf = valor - desc
print('O preço do produto com desconto de 5% é de R$ {}'.format(vf))

========================================================================================================================

13- Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salario = int(input('Digite o salário: R$ '))
aumento = salario + (salario * 15 / 100)
print('O novo salário do funcionário e de R$ {}'.format(aumento))

========================================================================================================================

14- Faça um programa que converta graus C em graus F
C = float(input('Digite a temperatura em graus C: '))
F = C * 1.8 + 32
print('A temperatura em graus F é: {}'.format(F))

========================================================================================================================

15- Escreva um programa que pergunte a quantidade de KM rodados por um carro alugado e a quantidade de dias peloas quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado
km = float(input('Digite quantos km o carro rodou: '))
dia = int(input('Digite quantos dias o carro foi alugado: '))
total = (km * 0.15) + (dia * 60)
print('O valor a ser pago é de R${:.2f}'.format(total))

========================================================================================================================

16- Crie um programa que leia um número Real e mostre na sua tela a sua porção inteira (ex: 6.127 = 6)
num = float(input('Digite um número Real: '))
inteiro = int(num)
print('O número {} tem a parte inteira {}'.format(num, inteiro))
import math
num = float(input('Digite um número Real: '))
inteiro = math.floor(num)
print('O número {} tem a parte inteira {}'.format(num, inteiro))

========================================================================================================================

17- Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
mostre o comprimento da hipotenusa
from math import hypot
cat_op = float(input('Informe o comprimento do cateto oposto: '))
cat_ad = float(input('Informe o comprimento do cateto adjacente: '))
hip = hypot(cat_op, cat_ad)
print('O valor da hipotenusa é: {:.2f}'.format(hip))

========================================================================================================================

18- Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import radians, sin, cos, tan
angulo = int(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(' Ângulo: {}\n Seno: {:.2f}\n Cosseno: {:.2f}\n Tangente: {:.2f}'.format(angulo,seno,cosseno,tangente))

========================================================================================================================

19- Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
nome deles e escrevendo o nome do escolhido.
from random import choice
sortear = []
nome1 = input('Digite o nome do primeiro aluno: ')
sortear.append(nome1)
nome2 = input('Digite o nome do segundo aluno: ')
sortear.append(nome2)
nome3 = input('Digite o nome do terceiro aluno: ')
sortear.append(nome3)
nome4 = input('Digite o nome do quarto aluno: ')
sortear.append(nome4)
print(sortear)
print('O aluno escolhido é: {}'.format(choice(sortear)))

========================================================================================================================

20- O mesmo professor do desafio anterior que sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
ordem = []
nome1 = input('Digite o nome do primeiro aluno: ')
ordem.append(nome1)
nome2 = input('Digite o nome do segundo aluno: ')
ordem.append(nome2)
nome3 = input('Digite o nome do terceiro aluno: ')
ordem.append(nome3)
nome4 = input('Digite o nome do quarto aluno: ')
ordem.append(nome4)
print(ordem)
random.shuffle(ordem)
print('A ordem de apresentação é: 1-{} 2-{} 3-{} 4-{}'.format(ordem[0], ordem[1], ordem[2], ordem[3]))

========================================================================================================================

21- Faça um programa em python que abra e reproduza o áudio de um arquivo MP3
import playsound
playsound.playsound('Human.mp3')

========================================================================================================================

22- Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiusculas
O nome com todas as letras minusculas
Quantas letras ao todo(sem considerar os espaços)
Quantas letras tem o primeiro nome
nome = input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
junto = nome.replace(' ','')
print(len(junto))
divido = nome.split()
print(len(divido[0]))

========================================================================================================================

23- Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))

========================================================================================================================

24- Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
cidade = input('Digite o nome de uma cidade: ')
nome = cidade.title()
if 'Santo' in nome:
    print('Começa com o nome Santo')
else:
    print('Não começa com o nome Santo')

========================================================================================================================

25- Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = input('Digite o seu nome: ')
caixa_alta = nome.title()
if 'Silva' in caixa_alta:
    print('Tem Silva')
else:
    print('Não tem Silva')

========================================================================================================================

26- Faça um programa que leia uma frase pelo teclado e moestre:
Quantas vezes aparece a leta 'A'
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez
frase = input('Digite uma frase: ')
baixo = frase.lower()
baixo.strip()
print(baixo.count('a'))
print(baixo.find('a')+1)
print(baixo.rfind('a')+1)

========================================================================================================================

27- Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separado
nome = input('Digite seu nome completo: ').strip()
separado = nome.split()
print(separado[0])
print(separado[-1])

========================================================================================================================

28- Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O computador deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
print('Gerando um número entre 0 e 5...')
num = randint(0, 5)
dig = int(input('Digite um número entre 0 e 5: '))

if num == dig:
    print('Você venceu!')
else:
    print('Você perdeu!')
print('Você digitou {} e eu escolhi o {}'.format(dig, num))

========================================================================================================================

29- Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
ele foi multado. A multa vai custar R$7,00 por cada Km acimda do limite
vel = int(input('Digite a velocidade do carro: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi multado! O valor da multa é de R${}'.format(multa))
else:
    print('Siga!')

========================================================================================================================

30- Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
num = int(input('Digite um número: '))
if (num % 2) == 0:
    print('Numero PAR')
else:
    print('ÍMPAR')

========================================================================================================================

31- Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.
dis = int(input('Digite a distância da viagem em Km: '))
if dis <= 200:
    valor = dis * 0.50
    print('O valor da viagem é de R${}'.format(valor))
else:
    valor = dis * 0.45
    print('O valor da viagem é de R${}'.format(valor))

========================================================================================================================

32- Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.
ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    print('bissexto')
else:
    print('Normal')

========================================================================================================================

33- Faça um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('Menor:{} '.format(menor))
print('Maior:{} '.format(maior))

========================================================================================================================

34- Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$ 1250,00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Digite seu salário: R$'))
if salario > 1250.00:
    novo_salario = (salario * 0.10) + salario
    print('O aumenteo de 10% do salario R${} é de R${}'.format(salario, novo_salario))
else:
    novo_salario = (salario * 0.15) + salario
    print('O aumente de 15% do salario R${} é de R${}'.format(salario, novo_salario))

========================================================================================================================

35- Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou não formar um
triângulo
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')

========================================================================================================================

36-Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não
pode exceder 30% do salário ou então o empréstimo será negado
casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário: R$'))
anos = int(input('Digite em quantos anos você vai pagar: '))
mes = anos * 12
prestacao = casa / mes
minimo = salario * 0.30

if prestacao <= minimo:
    print('O valor da prestação a ser paga será de R${}'.format(prestacao))
else:
    print('Emprestimo negado')

========================================================================================================================

37- Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 Binario
2 octal
3 Hexadecimal
num = int(input('Digite um número inteiro: '))
base = int(input('Digite qual a abse de conversão desejada:\n'
                 '1 - Binário\n'
                 '2 - Octal\n'
                 '3 - Hexadecimal\n'
                 ''))
if base == 1:
    print(format(num, 'b'))
elif base == 2:
    print(format(num, 'o'))
else:
    print(format(num, 'x'))

========================================================================================================================

38- Escreva um programa que leia dois número inteiros e compare-os, mostrando na tela uma mensagem:
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais
n1 = int(input('Digite o prmeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro número é maior'.format(n1))
elif n2 > n1:
    print('O segundo número é maior'.format(n2))
else:
    print('Não existe valor maior, os dois ({} e {}) são iguais'.format(n1, n2))

========================================================================================================================

39- Faça um programa que eleia o ano de um nascimento de um jovem e informe, de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar
Se é a hora de se alistar
Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print('Você tem {} anos'.format(idade))

if idade < 18:
    print('Você ainda vai se alistar')
    contagem = 18 - idade
    print('Falta(m) {} ano(s) para seu alistamento'.format(contagem))
elif idade == 18:
    print('Está na hora do seu alistamento')
else:
    print('Você já passou do tempo de alistamento')
    contagem = idade - 18
    print('Já se passaram {} ano(s) do seu alistamento'.format(contagem))
========================================================================================================================

40- Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
a média atingida:
Media abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('A sua média é: {}. REPROVADO!'.format(media))
elif media >= 7:
    print('A sua média é: {}. APROVADO!'.format(media))
else:
    print('A sua média é {}. RECUPERAÇÃO!'.format(media))

========================================================================================================================

41- A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria de acordo com a idade:
Até 9 nos:MIRIM
Até 14 anos:INFANTIL
até 19 anos:JUNIOR
até 20 anos:SENIOR
acima:MASTER

from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print(idade)
if idade <= 9:
    print('Mirim')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Junior')
elif idade > 19 and idade <= 25:
    print('Senior')
else:
    print('Master')

========================================================================================================================

42- Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero: todos os lados iguais
Isósceles: dois lados iguais
Escaleno: todos os lados diferentes

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo')
    if r1 == r2 and r1 == r3:
        print('Triângulo Equilátero')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')
else:
    print('Não pode formar um triângulo')


========================================================================================================================

43- Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
tabela abaixo:
Abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade mórbida

kg = float(input('Digite seu peso em Kg: '))
alt = float(input('Digite sua altura em mts: '))
imc = kg / (alt * alt)
if imc < 18.5:
    print('Abaixo do peso. IMC = {:.2f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal. IMC = {:.2f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Sobrepeso. IMC = {:.2f}'.format(imc))
elif imc >= 30 and imc < 40:
    print('Obesidade. IMC = {:.2f}'.format(imc))
else:
    print('Obesidade mórbida. IMC = {:.2f}'.format(imc))

========================================================================================================================

44- Elabore um programa que calcule o valor a  ser pago por um produto, consideranto o seu preço normal e condição de
pagamento:
A vista dinheiro/cheque: 10% de desconto
A vista no cartão: 5% de desconto
Em até 2x no cartão: preço normal
3x ou amis no cartão: 20% de juros

preco = float(input('Digite o valor do produto: R$'))
pagamento = int(input('Infome o método de pagamento(onde):\n'
                  '1 -A vista dinheiro/cheque\n'
                  '2 -A vista cartão\n'
                  '3 -Em até 2x no cartão\n'
                  '4 -Em 3x ou mais no cartão\n'
                  ''))
if pagamento == 1:
    print('PAGAMENTO A VISTA DINHEIRO OU CHEQUE')
    valor = preco - (preco * 0.10)
    print('O valor do produto com 10% de desconto é de R${}'.format(valor))
elif pagamento == 2:
    print('PAGAMENTO A VISTA CARTÃO')
    valor = preco - (preco * 0.05)
    print('O valor do produto com 5% de desconto é de R${}'.format(valor))
elif pagamento == 3:
    print('PAGAMENTO EM ATÉ 2X NO CARTÃO')
    print('O valor do produto é de R${}'.format(preco))
else:
    print('3X OU MAIS NO CARTÃO')
    valor = preco + (preco * 0.20)
    print(('O valor do produto é de R${}'.format(valor)))

========================================================================================================================

45- Crie um programa que faça o computador jogar Jokenpô com você

from random import randint
from time import sleep
pc = randint(1, 3)
print('-=-' *10)
print('VAMOS JOGAR JOKENPÔ!!!')
print('-=-' *10)
jogador = int(input('Digite a opção desejada, onde:\n'
                    '1- Pedra\n'
                    '2- Papel\n'
                    '3- Tesoura\n'
                    ''))
print('-=-' *10)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!!')
if pc == jogador:
    print('EMPATE')
elif pc == 1 and jogador == 2:
    (print('JOGADOR GANHOU!\n'
           'PC = Pedra\n'
           'JOGADOR = Papel'))
elif pc == 1 and jogador == 3:
    print('PC GANHOU!\n'
          'PC = Pedra\n'
          'JOGADOR = Tesoura')
elif pc == 2 and jogador == 1:
    print('PC GANHOU!\n'
          'PC = Papel\n'
          'JOGADOR = Pedra')
elif pc == 2 and jogador == 3:
    print('JOGADOR GANHOU!\n'
          'PC = Papel\n'
          'JOGADOR = Tesoura')
elif pc == 3 and jogador == 1:
    print('JOGADOR GANHOU!\n'
          'PC = Tesoura\n'
          'JOGADOR = Pedra')
elif pc == 3 and jogador == 2:
    print('PC GANHOU!\n'
          'PC = Tesoura'
          'JOGADOR = Papel')

========================================================================================================================

46- Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles

from time import sleep
for n in range(10,-1,-1):
    print(n)
    sleep(1)
print('BUM')

========================================================================================================================

47- Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

print('Os números pares entre 1 e 50 são:')
for n in range(0, 50, 2):
    print(n)

========================================================================================================================

48- Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
intervalo de 1 até 500

soma = []
for n in range(1, 501, 2):
    if n % 3 == 0:
        print(n)
        soma.append(n)
print(sum(soma))

========================================================================================================================

49- Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o for

num = int(input('Digite um número: '))
for n in range(0, 11):
    mult = n * num
    print('{} x {} = {}'.format(n, num, mult))

========================================================================================================================

50- Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquelas que forem pares. Se o valor
digitado for ímpar, desconsidere-o

soma = 0
cont = 0
for n in range(1, 7):
    num = int(input('Digite o {} valor: '.format(n)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))

========================================================================================================================

51- Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão

p1 = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
decimo = p1 + (10 - 1) * r

for n in range(p1, decimo + r, r):
    print('{}'.format(n), end='-> ')
print('Acabou')

========================================================================================================================

52- Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número: '))
tot = 0
for n in range(1, num + 1):
    if num % n == 0:
       print('\033[33m', end='')
       tot = tot + 1
    else:
        print('\033[31m', end='')
    print('{}'.format(n),end=' ')
print('\n\033[mO numero {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('O número é primo')
else:
    print('Não é primo')

========================================================================================================================

53- Crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderando os espaços

frase = str(input('Digite algo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não é um palìndromo')

========================================================================================================================

54- Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atigiram a
maioridade e quantas já são maiores

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nascimento = int(input('Digite o {}ª data de nascimento: '.format(c)))
    maioridade = atual - nascimento
    if maioridade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('{} maior de idade'.format(totmaior))
print('{} menor de idade'.format(totmenor))

========================================================================================================================

55- Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lidos;

maior = 0
menor = 0
for n in range(1, 6):
    peso = int(input('Digite o {}º peso: '.format(n)))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior peso: {}'.format(maior))
print('Menor peso: {}'.format(menor))


========================================================================================================================

56- Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
A média de idade do grupo
Qual é o nome do homem mais velho
Quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('---{}ª PESSOA---'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média é {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))

========================================================================================================================

57- Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto.

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo ("M" ou "F"): ')).upper()
print('Sexo {} válido!'.format(sexo))

========================================================================================================================

58- Melhore o desafio 28 onde o computador vai "pensar" em um número entre 0 a 10. Só que agora o jogador vai tentar
advinhar até acertar, mostrando no final quantos palpites foram necessários.

from random import randint
print('Gerando um número entre 0 e 10...')
num = randint(0, 11)
erro = 0

dig = ''
while num != dig:
    dig = int(input('Digite um número entre 0 e 10: '))
    if dig != num:
        print('Errou, tente novamente')
        erro += 1
    else:
        print('Acertou!')
print('Fim! \nVocê acertou o número {} gerado e precisou de {} vezes para acertar'.format(num, erro + 1))

========================================================================================================================

59- Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))

opcao = 0
while opcao != 5:
    print('-=' * 20)
    opcao = int(input('Escolha uma opção: \n'
                      '[1] somar\n'
                      '[2] multiplicar\n'
                      '[3] maior\n'
                      '[4] novos números\n'
                      '[5] sair do programa\n'
                      ''))
    print('-=' * 20)
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre o {} e {} é: {}'.format(n1, n2, soma))
    if opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre o {} e {} é: {}'.format(n1, n2, mult))
    if opcao == 3:
        max = max(n1, n2)
        print('O maior número entre o {} e o {} é: {}'.format(n1, n2, max))
    if opcao == 4:
        n1 = int(input('Digite o novo valor do 1º número: '))
        n2 = int(input('Digite o novo valor do 2º número: '))
        print('Os novos valores digitados são {} e {}'.format(n1, n2))
    if opcao == 5:
        print('Fim')
        exit()

========================================================================================================================

60- Faça um programa que leia um número qualquer e mostre o seu fatorial. (ex.: 5! = 5x4x3x2x1 = 120

from math import factorial
num = 9999
while num != 0:
        num = int(input('Digite um número ou 0 para sair: '))
        print('O fatorial do número {} é: {}'.format(num, factorial(num)))
print('Fim')

========================================================================================================================

61- Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while

print('-=-' *10)
p1 = int(input('Primeiro Termo: '))
r = int(input('Digite a razão: '))
termo = p1
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('FIM')

========================================================================================================================

62- Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
ele disser qu quer mostrar 0 termos.

print('-=-' *10)
p1 = int(input('Primeiro Termo: '))
r = int(input('Digite a razão: '))
termo = p1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('...')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Fim')

========================================================================================================================

63- Escreva um programa que leia um número N inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência
de fibonacci (ex.: 0, 1, 1, 2, 3, 5, 8)

print('-' *30)
print('SEQUÊNCIA DE FIBONACCI')
print('-' *30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')

========================================================================================================================

64- Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
(desconsiderando o flag)
lista = []
num = 0
while num != 999:
    num = int(input('Digite um número ou 999 para sair: '))
    if num != 999:
        lista.append(num)
print(lista)
print('A soma dos valores digitados é: {}'.format(sum(lista)))

========================================================================================================================

65- Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant ==1:
      maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

========================================================================================================================

66- Crie um programa que leia vários números inteiro s pelo teclado. O programa só vai parar quando o usuário digitar 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles

soma = cont = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos números digitados é: {soma}')
print(f'Foram digitados {cont} números')

========================================================================================================================

67- Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Digite um número para mostrar a tabuada: '))
    if num < 0:
        print('FIM')
        break
    print('=-='*14)
    print(f'TABUADA DO {num}:')
    for n in range(1, 11):
        print(f'{num} x {n} = {num * n}')
        n += 1
    print('=-=' * 14)

========================================================================================================================

68- Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint
v = 0
while True:
    jog = int(input('Digite um valor: '))
    comp = randint(0, 11)
    tot = jog + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jog} e o computador {comp}. total de {tot}')
    if tipo == 'P':
        if tot % 2 == 0:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break

    elif tipo == 'I':
        if tot % 2 == 1:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    print('Vamos jogar novamente!')
print(f'GAME OVER!Você venceu {v} vezes')

========================================================================================================================

69- Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final mostre:
A) quantas pessoas tem mais de 18 anos
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.

maior = homem = mu20 = cont = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [F/M] ')).strip().upper()[0]
    cad = ' '
    while cad not in 'SN':
        cad = str(input('Deseja continuar o cadastro? [S/N] ')).strip().upper()[0]
    cont += 1
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mu20 += 1
    if cad == 'N':
        break

print('*=*' *12)
print(f'Foram cadastrados {cont} pessoas onde:')
print(f'{maior} pessoa(s) tem mais de 18 ano(s)')
print(f'{homem} homen(s) cadastrado(s)')
print(f'{mu20} mulhere(s) com menos de 20 anos')
print('*=*' *12)

========================================================================================================================

70- Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
No final mostre:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato

maior1k = total = menor = cont = 0
barato = ' '
print('=' *25)
print('{:^25}'.format('COMPRA DE PRODUTOS'))
print('=' *25)
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto R$'))
    cont += 1
    total += preco
    if preco > 1000:
        maior1k += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto

    cad = ' '
    while cad not in 'SN':
        cad = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    print('-' *25)
    if cad == 'N':
        break
print(f'O total da compra é de R${total:.2f}')
print(f'Tem {maior1k} produto(s) acima de R$ 1000,00')
print(f'O produto mais barato é {barato} R${menor:.2f}')

========================================================================================================================

71- Crie um prorama que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs, Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

print('=' *25)
print('{:^25}'.format('CAIXA ELETRÔNICO'))
print('=' *25)
valor = int(input('Qual o valor de saque? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

========================================================================================================================

72- Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extenso, de zero até vinte;
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

num = int(input('Digite um número entre 0 e 20: '))
while num not in range(0, 21):
    print('Tente novamente')
    num = int(input('Digite um número entre 0 e 20: '))
ext = ('zero', 'um', 'dois', 'três', 'quarto', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezessei', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(f'Você digitou o número {ext[num]}')

========================================================================================================================

73-Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de
colocação. Depois mostre:
A) APenas os 5 primeiros colocados.
B) Os ultimos 4 colcoados da tabela
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela está o time da Chapecoense

Times =  (Cor, Pal, San, Gre, Cru, Fla, Vas, Cha, AtM, Bot, Apr, Bah, Sao, Flu, Sre, EcV, Ava, Pop, Agt)

print('-' *22)
print('CAMPEONATO BRASILEIRO')
print('-' *22)
times = ('Cor', 'Pal', 'San', 'Gre', 'Cru', 'Fla', 'Vas', 'Cha', 'AtM', 'Bot', 'Apr', 'Bah', 'Sao', 'Flu', 'Sre', 'EcV',
         'Ava', 'Pop', 'Agt')
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Os 4 últimos colocados são: {times[-4:]}')
print(f'Tabela dos times em ordem aletória: {sorted(times)}')
print(f"A Chapecoense está na {times.index('Cha')+1}ª posição")

========================================================================================================================

74-Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
print('Gerando 5 números aleatórios...')
num = (randint(0,100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Os números gerados foram: {num}')
print(f'O maior número gerado é: {max(num)}')
print(f'O menor número gerado e: {min(num)}')

========================================================================================================================

75-Desenvolva um programa que leia quatro valores pelo telcado e guarde-os em uma tupla. No final, mostre:
A) QUantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) QUais foram os números pares

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))
n4 = int(input('Digite o 4º valor: '))
numeros = (n1, n2, n3, n4)
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 foi digitado na {numeros.index(3)+1}ª vez')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 ==0:
        print(n,end=' ')

========================================================================================================================

76- Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final
mostre uma listagem de preços organizando os dados em forma tabular

tabela = ('Lápis', 1.75,
          'Borracha', 2.00,
          'Caderno', 15.90,
          'Estojo', 25.00,
          'Transferidor', 4.20,
          'Compasso', 9.99,
          'Mochila', 120.32,
          'Canetas', 22.30,
          'Livro', 34.90)
print('-' *40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' *40)
for pos in range(0, len(tabela)):
    if pos % 2 == 0:
        print(f'{tabela[pos]:.<30}',end='')
    else:
        print(f'RS{tabela[pos]:>7.2f}')
print('-' *40)

========================================================================================================================

77- Crie um programa que tenha uma tupla com várias palavras (não usar acentos) depois disso, você deve mostrar pra cada
palavra quais são suas vogais

palavras = ('APRENDER',
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'GRATIS',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMADOR',
            'FUTURO')
for n in palavras:
    print(f'\nA palavra {n} tem ', end='')
    for letra in n:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')

========================================================================================================================

78-Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor difitado e as suas respectivas posições na lista

lista = []
for n in range(0, 5):
    lista.append(int(input('Digite um número: ')))
print(f'O maior número digitado é: {max(lista)} e está na posição {lista.index((max(lista)))}')
print(f'O menor número digitado é: {min(lista)} e está na posição {lista.index(min(lista))}')

========================================================================================================================

79-Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro ele não será adicionado. No final, serão exibidos todos os valores únicos difitados, em ordem crescente.

lista = []
dec = ''
num = (int(input('Digite um número: ')))
lista.append(num)
print('Número adicionado com sucesso!')
print('-' * 30)

while True:
    dec = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if dec == 'S':
        num = (int(input('Digite um número: ')))
        if num not in lista:
            print('Número adicionado com sucesso!')
            print('-' * 30)
            lista.append(num)
        else:
            print('Número já adicionado a lista')
            print('-' * 30)
    if dec == 'N':
        break
print(f'Os números digitados em ordem crescente é: {sorted(lista)}')

num = []
while Truelista = []
dec = ''
num = (int(input('Digite um número: ')))
lista.append(num)
print('Número adicionado com sucesso!')
print('-' * 30)

while True:
    dec = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if dec == 'S':
        num = (int(input('Digite um número: ')))
        if num not in lista:
            print('Número adicionado com sucesso!')
            print('-' * 30)
            lista.append(num)
        else:
            print('Número já adicionado a lista')
            print('-' * 30)
    if dec == 'N':
        break
print(f'Os números digitados em ordem crescente é: {sorted(lista)}')


lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Número adicionado com sucesso!')
    else:
        print('Número já adicionado')
    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if r in 'N':
        break
print('-' * 30)
print(f'Os valores em ordem crescente são: {sorted(lista)}')

========================================================================================================================

80-Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem ursar o sort()). No final, mostre a lista ordenada na tela;

lista = []
maior = menor = 0
for n in range(0, 5):
    num = int(input('Digite um número: '))

    if n == 0:
        lista.append(num)
    elif num < lista[0]:
            lista.insert(0, num)
    elif num < lista[-1]:
        lista.insert(-1,num)
    else:
        lista.append(num)
    print(lista)

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Os valores digitados em ordem foram')

========================================================================================================================

81-Crie um programa que vai ler vários números e colcoar em uma lsita. Depois disso, mostre:
A) QUantos números foram difitados
B) A lista de valores, ordenada de forma decrescente
C) Se o valor 5 foi difitado e está ou não na lista

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
print(f'Você digitou {len(lista)} elementos')
print(lista)
lista.sort(reverse=True)
print(f'Os valores da lista em ordem decresente é: {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')


========================================================================================================================

82-Crie um preograma que vai ler vários números e colocar em uma lista. Depois disso, crei duas listas extras que
vão conter apenas os valores pares e os valores ímpares difitados, respectivamente. Ao final, mostre o conteúdo das
3 listas geradas

lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('QUer continuar? [S/N]')).upper().strip()[0]
    if r == 'N':
        break

for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f'A lista dos valores digitados é: {lista}')
print(f'A lista com os números PARES é: {par}')
print(f'A lista com os números ÍMPARES é: {impar}')

========================================================================================================================

83-Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = str(input('Digite um expressão: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')

========================================================================================================================

84- Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

cadastro = []
dado = []
pesomai = pesomen = 0
while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(float(input('Digite o peso: ')))
    if len(cadastro) == 0:
        pesomai = pesomen = dado[1]
    else:
        if dado[1] > pesomai:
            pesomai = dado[1]
        if dado[1] < pesomen:
            pesomen = dado[1]
    cadastro.append(dado[:])
    dado.clear()
    dec = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if dec == 'N':
        break
print(f'Foram cadastradas {len(cadastro)} pessoas')
print(f'O maior peso é {pesomai}Kg. Peso de ', end='')
for p in cadastro:
    if p[1] == pesomai:
        print(f' [{p[0]}] ', end='')
print()
print(f'O menor peso é {pesomen}Kg. Peso de ', end='')
for p in cadastro:
    if p[1] == pesomen:
        print(f' [{p[0]}] ',end='')
print()

========================================================================================================================

85-Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final mostre os valores pares e ímpares em ordem crescente

lista = [[], []]
num = 0
for n in range(1,8):
    valor = int(input(f'Digite o {n}º número: '))
    if n % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f'Os valores digitados foram: {sorted(lista)}')
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram: {sorted(lista[1])}')

========================================================================================================================

86-Crie um programa que crie uma matriz de 3x3 e preencha com valores lidos pelo teclado
No final mostre a matriz na tela com a formatação correta

mat0 = [[], [], []]
mat1 = [[], [], []]
mat2 = [[], [], []]
num = []

for n in range(0, 3):
    num.append(int(input(f'Digite um valor para [0, {0+n}]: ')))
mat0[0].append(num[0])
mat0[1].append(num[1])
mat0[2].append(num[2])


for n in range(0, 3):
    num.append(int(input(f'Digite um valor para [1, {0+n}]: ')))
mat1[0].append(num[3])
mat1[1].append(num[4])
mat1[2].append(num[5])


for n in range(0, 3):
    num.append(int(input(f'Digite um valor para [2, {0+n}]: ')))
mat2[0].append(num[6])
mat2[1].append(num[7])
mat2[2].append(num[8])



print('-=' *30)
print(mat0)
print(mat1)
print(mat2)

OOOOOOOOOOOOOOOOOOOOOU

mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        mat[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' *30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{mat[linha] [coluna]:^5}]',end='')
    print()

========================================================================================================================

87- Aprimore o desafio anterior, mostrando no final
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha

mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        mat[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' *30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{mat[linha] [coluna]:^5}]',end='')
        if mat[linha][coluna] % 2 == 0:
            spar += mat[linha][coluna]
    print()

print(f'A soma dos valores pares é {spar}')
for linha in range(0, 3):
    scol += mat[linha][2]
print(f'A soma dos valores da terceira coluna é {scol}')

for coluna in range(0, 3):
    if coluna == 0:
        mai = mat[1][coluna]
    elif mat[1][coluna] > mai:
        mai = mat[1][coluna]
print(f'O maior número da segunda linha é {mai}')


========================================================================================================================

88-Faça um programa que ajuda um jogador da Mega sena a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint
lista = list()
jogos = list()
print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')

========================================================================================================================

89-Crie um programa que leia nome e duas notas de vários alunos e guarde tudo e uma lista composta. No final, mostre
um bolteim contendo a média de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1+nota2) / 2
    ficha.append([nome, [nota1,nota2], media])
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'{"No.":<3}{"NOME":<10}{"MÉDIA":>10}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

========================================================================================================================

90-Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre
o conteúdo da estrututra na tela

ficha = {}
ficha['nome'] = str(input('Digite o nome do Aluno: '))
ficha['media'] = float(input(f'Digite a média de {ficha["nome"]}: '))
if ficha['media'] > 5:
    ficha['situacao'] = 'Aprovado'
else:
    ficha['situacao'] = 'Reprovado'

print('-=' * 30)
for k, v in ficha.items():
    print(f'- {k} é igual a {v}')

========================================================================================================================

91-Crie um porgrama onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior numero no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

========================================================================================================================

92-Crie um programa que leia nome, ano de nascimento e carteira dfe trabalho e cadastre-os (com idade) em um dicionário
se por acaso a CTPS for difrente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar

from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Digite o nome: '))
nasc = int(input('Digite o ano de nascimento (xxxx): '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['ctps'] = int(input('Digite a carteira de trabalho (0 não tem): '))
if cadastro['ctps'] > 0:
    cadastro['contratacao'] = int(input('Digite o ano da contratação (xxxx): '))
    cadastro['salario'] = float(input('Digite o salário: R$ '))
    trabalhado = datetime.now().year - cadastro['contratacao']
    restante = 35 - trabalhado
    cadastro['idade_apo'] = cadastro['idade'] + restante

    print('-=' * 30)
    for k, v in cadastro.items():
        print(f'- {k} tem o valor {v}')


else:
    print('-=' * 30)
    for k, v in cadastro.items():
        print(f'- {k} tem o valor {v}')

========================================================================================================================

93-Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado
em um dicionário, inclunindo o totla de gols feitos durante o campeonato.

analise = {}
gol_partida = []
partida = 1
analise['nome'] = str(input('Digite o Nome: '))
partidas = int(input(f'Informe quantas partidas o jogador {analise["nome"]} jogou: '))
for n in range(0, partidas):
    gol_partida.append(int(input(f'Quantos gol(s) o jogador {analise["nome"]} fez na partida {n+1}: ')))
gol_tot = sum(gol_partida)


analise['partidas'] = partidas
analise['gol_partida'] = gol_partida[:]
analise['gol_tot'] = gol_tot

print('-=' * 30)
print(analise)
print('-=' * 30)
for k, v in analise.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

print(f'O jogador {analise["nome"]} jogou {partidas} partidas onde:')
for n in range(0, analise['partidas']):
    print(f'=> Na partida {partida}, fez {gol_partida[n]}')
    partida += 1
print(f'Foi um total de {analise["gol_tot"]} gols.')

========================================================================================================================

94-Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre:
A) QUantas pessoas foram cadastradas
B) A média de idade do grupo.
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da media

geral = []
pessoa = {}
soma = media = 0
while True:
    pessoa['nome'] = str(input('Digite o Nome: '))
    pessoa['sexo'] = str(input('Informe o Sexo [M/F]: ')).upper().strip()[0]
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        pessoa['sexo'] = str(input('Informe o Sexo [M/F]: ')).upper().strip()[0]

    pessoa['idade'] = int(input('Digite a Idade: '))
    soma += pessoa['idade']
    geral.append(pessoa.copy())
    dec = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    while dec not in 'SN':
        print('ERRO! Responda apenas S ou N')
        dec = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if dec == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(geral)} pessoas cadastradas.')
media = soma / len(geral)
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in geral:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ', end='')
for p in geral:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('<< ENCERRANDO >>')

========================================================================================================================

95- Aprimore o desafio 93 para que ele funciona com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador

time = []
analise = {}
gol_partida = []
partida = 1

while True:
    analise.clear()
    analise['nome'] = str(input('Digite o Nome: '))
    partidas = int(input(f'Informe quantas partidas o jogador {analise["nome"]} jogou: '))
    for n in range(0, partidas):
        gol_partida.append(int(input(f'Quantos gol(s) o jogador {analise["nome"]} fez na partida {n+1}: ')))
    gol_tot = sum(gol_partida)
    time.append(analise.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
analise['partidas'] = partidas
analise['gol_partida'] = gol_partida[:]
analise['gol_tot'] = gol_tot

print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

========================================================================================================================

96-Faça um programa que tenha um função chama área(), que receba as dimensões de um terreno retangular(largura e
comprimento) e mostre a área do terreno

def area(l, c):
    tot = l * c
    print(f'A área de um terreno {l}x{c} é de {tot}m²')


def linha():
    print('-' * 30)


print('Controle de Terrenos')
linha()
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
linha()
area(l, c)

========================================================================================================================

97- Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável. Ex escreva('Ola mundo!')
saida:
---------------
  Ola mundo!
---------------

def escreva(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)


escreva('Alô Mundo')
escreva('Alvaro Ito')
escreva('Curso de Python no Youtube')
escreva('Cev')

========================================================================================================================

98-Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e realize
a contagem. Seu programa tem que realizar tres contagens atraves da função criada:
A) De 1 até 10, de 1 em 1
B) de 10 até 0, de 2 em 2
C) Uma contagem personalizada

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até o {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

========================================================================================================================

99-Faça um programa que tenha um função chamada maior(), que receba varios parametros com valores inteiros. Seu programa
 tem que analisar todos os valores e dizer qual deles é o maior

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('\nAnalisando os valores passados...')
    for n in num:
        print(f'{n}', end=' ')
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

========================================================================================================================

100-Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira
função vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os
valores pares sorteados pela função anterior

from random import randint
numeros = []
def sorteia(lista):
    for n in range(5):
        lista.append(randint(0,10))
    print(f'Sorteando 5 valores da lista: {lista} PRONTO!')


def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {lista}, temos {soma}')

sorteia(numeros)
somaPar(numeros)

========================================================================================================================

101- Crie um programa que tenha um função chamada voto() que vai recever como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoal tem ovoto negado, opcional ou obrigatório nas eleições

def voto(ano):
    from datetime import datetime
    atual = datetime.now().year
    print('-' * 40)
    idade = atual - nascimento
    if 16 <= idade <= 17 or idade > 70:
        status = 'VOTO OPCIONAL'
    elif idade < 16:
        status = 'NÃO VOTA'
    else:
        status = 'VOTO OBRIGATÓRIO'

    print(f'Com {idade} anos: {status}')

nascimento = int(input('Digite o ano de nascimento (xxxx): '))
voto(nascimento)

========================================================================================================================

102- Crie um programa que tenha um função fatorial() que receba dois parâmetros: o primeiro que indique o número a
calcular e o outro chamado show, que será um valor lógico (opcinonal) indicando se será mostrado ou na tela o processo
de cálculo do fatorial.

def fatorial(num,show=False):

    Calcular o fatorial de um número
    :param num: Número para calcular o fatorial
    :param show: se irá ou não mostrar o fatorial detalhado
    :return: retorna o fatorial de um número digitado

    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show == False:
        return f
    else:
        cont = n
        while cont > 0:
            print(f'{cont}',end='')
            print(' x ' if cont > 1 else ' = ', end='')
            cont -= 1
        return f



n = int(input('Digite um número: '))
print(fatorial(n, True))
help(fatorial)

========================================================================================================================

103- Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
sido informado corretamente.

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


#Programa Principal
nome = str(input('Nome do Jogador: '))
gol = str(input('Número de Gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gol=gol)
else:
    ficha(nome, gol)

========================================================================================================================

104- Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a função input() do Python, só
que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaint('Digite um n')

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO!Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


#Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

========================================================================================================================

105- Faça um programa que tenha um função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings da função

def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] > 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

#Programa Principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)

========================================================================================================================

106- Faça um mini-sistema que utilize o interactive help do Python. O usuário vai digitar o comando e o manul vai
aparecer. Quando o usuário digitar a palavra 'Fim', o programa se encerrará; OBS: use cores

from time import sleep
c = ('\033[m',        # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;30m'     # 6 - branco
     );

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)

========================================================================================================================

107- Crie um módulo chamado moedpy que tenha as funções incorpadas aumentar(), diminuir(), dobro() e metade(). Faça
também um programa que importe esse módulo e use algumas dessas funções

========================================================================================================================

108- Adpate o código do desafio 107, criando uma função adiciona chamada moeda() que consiga mostrar os valores como
um valor monetário formatado

========================================================================================================================

109- Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o
valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108

========================================================================================================================

110- Adicione ao módulo moedapy criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
informações geradas pelas funções que já temos no módulo criado até aqui

========================================================================================================================

111- Crie um pacote chamado utilidadescev que tenha dois módulos itnernos chamados moeda e dado. Transfira todas as
funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando

========================================================================================================================

112- dentro do pacote utilidadescev que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
leiadinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas
valores que sejam monetários.

========================================================================================================================

113- Reescreva a função leitaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um
número de tipo inválido. Aproveite e crie uma função leiafloat() com a mesma funcionalidade

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('Por favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return n



numint = leiaint('Digite um número Inteiro: ')
numfloat = leiafloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {numint} e o real foi {numfloat}')

========================================================================================================================

114-Crie um codigo em Python que teste se o site Pudim está acessível pelo computador usado

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print('Deu erro')
else:
    print('Tudo OK')

========================================================================================================================

115-Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto
simples. O sistema só vai ter 2 opções: cadastrar um nova pessoa e listar todas as pessoas cadastradas

========================================================================================================================

116-

========================================================================================================================


"""
'''

'''
num = [2, 8, 4, 7]
num.pop()
num.insert(1, 3)
num.append(6)
print(num)