import random
listaNomes = []

while True:
    escolha = int(input('Escolha uma das opções:\n'
                        '1 - Adicionar um novo nome: \n'
                        '2 - Deletar um nome específico: \n'
                        '3 - Vizualizar os nomes: \n'
                        '4 - Visualizar uma posição específica: \n'
                        '5 - Sortear um nome: \n'
                        '0 - finalizar o programa: \n'))

    match escolha:
        case 1:
            nome = str(input('Digite um nome: '))
            listaNomes.append(nome.upper())
        case 2:
            nome = str(input('Digite o nome que você deseja apagar: ')).upper()
            if nome in listaNomes:
                listaNomes.remove(nome.upper())
            else:
                print('Nome inexistente')
        case 3:
            print(listaNomes)

        case 4:
            posicao = int(input('Digite a posição: '))
            if posicao in listaNomes:
                if posicao - 1 <= len(listaNomes):
                    print(listaNomes[posicao - 1])
            else:
                print("Posiçao inexistente")
        case 5:
            aleatorio = random.randint(0, len(listaNomes))
            print(listaNomes[aleatorio])
        case 0:
            break
        case _:
            print('Opção inváliada')
