from ex107 import moeda

valor = float(input('Digite o preço: R$'))


print(f'A metade de R${valor} é R${moeda.metade(valor):.2f}')
print(f'O dobro de R${valor} é R${moeda.dobro(valor)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(valor, 10)}')



