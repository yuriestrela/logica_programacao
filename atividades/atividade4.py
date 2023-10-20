from unittest import case

print('Bem vindo ao banco YuriBank!')
nome = (input('Digite seu nome: '))
print('Seu valor na conta é de R$1000,00')
saldo = 1000

while True:
    escolha = input('Escolha uma opção:\n'
                    '1 - Depositar\n'
                    '2 - Sacar\n'
                    '3 - Transferir\n'
                    '4 - Ver saldo\n')
    if escolha.isdigit():
        match escolha:
            case '1':
                soma = float(input('Digite o valor que você deseja depositar: '))
                    if soma > 0:
                        saldo += soma
                    else:
                        print('Impossível depositar um valor negativo!')


            case '2':
                subtracao = float(input('Digite o valor que você deseja sacar:'))
                if subtracao < saldo:
                    saldo -= subtracao
                else:
                    print('Saldo insuficiente!')
            case '3':
                print('Essa opção não está disponível no momento, tente outra opcão!')
            case '4':
                print(f'Seu saldo é de R${saldo}.')
    else:
        print('Digite apenas um número!')
      
