from random import choice


def sorteio(sorte):
    computador = choice(sorte)
    print(f'O computador escolheu {computador}\n')
    return computador


def jogo(usuario, computador):
    if usuario == 'pedra' and computador == 'tesoura':
        print('Você ganhou!')

    elif usuario == 'tesoura' and computador == 'papel':
        print('Você ganhou!')

    elif usuario == 'papel' and computador == 'pedra':
        print('Você ganhou!')

    elif usuario == computador:
        print('Empate!')

    else:
        print('Você perdeu!')

sorte = ['pedra', 'papel', 'tesoura']

for i in range(5):
    usuario = input('Pedra, papel ou tesoura? \n').lower()
    jogo(usuario, sorteio(sorte))
    print(20*"---")
    print(5*'\n')
  
