lista = []
listaPares = []
listaImpares = []
tuplaImpares = ([listaImpares])
for i in range(10):
    numero = int(input('Digite um número: '))
    lista.append(numero)
for numeros in lista:
    if numeros % 2 == 0:
        listaPares.append(numeros)
    elif numeros % 2 != 0:
        listaImpares.append(numeros)
print(f'Lista com números pares: {listaPares}.')
print(f'Tupla com números ímpares: {tuplaImpares}')
print(f'Possuem {len(listaPares)} números pares e {len(listaImpares)} números ímpares.')
print(f'A soma dos números pares é {sum(listaPares)} e a soma dos números ímpares é {sum(listaImpares)}\n'
      f'Já a soma de todos os números é {sum(lista)}.')
