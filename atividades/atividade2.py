# Questão 1
a = int(input('Quantos segundos tem o funcionamento da fábrica? '))

def horas(a):
    return a // 3600

b = a % 3600
def minutos(b):
    return b // 60

c = b % 60
def segundos(c):
    return c

print(f'A fábrica funciona {horas(a)} horas, {minutos(b)} minutos e {segundos(c)} segundos.')#


# Questão 2
a = int(input('Diga sua idade em anos: '))
m = int(input('Diga sua idade em meses: '))
d = int(input('Diga sua idade em dias: '))

def anos(a):
    return a * 365
def meses(m):
    return m * 30
def dias(d):
    return d
soma = anos(a) + meses(m) + dias(d)
print(f'Você tem {soma} dias.')
