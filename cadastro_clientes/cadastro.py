# Um dicionário chamado 'pacientes' será usado para armazenar informações dos pacientes.
pacientes = dict()

# Um identificador 'id' é inicializado para controlar os pacientes.
id = 1


# Função para cadastrar pacientes no dicionário 'pacientes'.
def cadastrar_pacientes(nome, idade, peso, altura):
    # Adiciona um novo paciente com um id único no dicionário 'pacientes'.
    pacientes[id] = [nome, idade, peso, altura]
    return "Paciente cadastrado com sucesso, pressione Enter para continuar:"


# Função para verificar se uma string contém apenas caracteres alfabéticos.
def verificacao_str(valor):
    validacao = True
    for i in valor:
        if i.lower() not in "abcdefghijklmnopqrstuvwxyz ":
            validacao = False
    return validacao


# Função para verificar se uma string contém apenas dígitos e um ponto decimal.
def verificacao_float(valor):
    validacao = True
    for i in valor:
        if i not in "1234567890.":
            validacao = False
    return validacao


# Função para verificar se uma string contém apenas dígitos.
def verificacao_int(valor):
    validacao = True
    for i in valor:
        if i not in "1234567890":
            validacao = False
    return validacao


# O programa principal começa aqui e é executado indefinidamente até que o usuário escolha encerrá-lo.
while True:
    # Solicita ao usuário que escolha uma opção do menu.
    escolha = int(input("""
Escolha uma das opções:
1 - Cadastrar novo paciente;
2 - Ver todos pacientes;
3 - Excluir paciente;
0 - Encerrar o sistema.
"""))

    # Estrutura de controle baseada no valor da escolha do usuário.
    match escolha:
        case 1:
            # Solicita informações do paciente ao usuário.
            nome = input("Digite o nome do paciente: ")
            idade = input("Digite a idade do paciente: ")
            peso = input("Digite o peso do paciente: ")
            altura = input("Digite a altura do paciente: ")

            # Verifica se as informações inseridas estão no formato correto.
            if verificacao_str(nome) and verificacao_int(idade) and verificacao_float(peso) and verificacao_float(
                    altura):
                # Converte as informações para os tipos de dados apropriados.
                idade = int(idade)
                peso = float(peso)
                altura = float(altura)

                # Chama a função para cadastrar o paciente e exibe uma mensagem de sucesso.
                input(cadastrar_pacientes(nome, idade, peso, altura))
                id += 1
            else:
                # Se as informações não estiverem no formato correto, exibe uma mensagem de erro.
                print("Informações fora do padrão.")
                input("Pressione Enter para continuar:")

            # Limpa a tela.
            print("\n" * 50)

        case 2:
            # Exibe informações de todos os pacientes cadastrados.
            for i in pacientes:
                print(f"O paciente com id: {i}, tem as seguintes informações:\n" +
                      f"nome: {pacientes[i][0]}\n" +
                      f"idade: {pacientes[i][1]}\n" +
                      f"peso: {pacientes[i][2]}\n" +
                      f"altura: {pacientes[i][3]}")
                print("________________________________________________________________")

            # Aguarda o usuário pressionar Enter para continuar.
            input("Pressione Enter para continuar")
            # Limpa a tela.
            print("\n" * 50)

        case 3:
            # Exibe a lista de pacientes com seus IDs.
            for i in pacientes:
                print(f"id: {i} - nome: {pacientes[i][0]}")

            # Solicita ao usuário o ID do paciente a ser excluído.
            deletar = input("Qual o id do paciente para ser deletado: ")

            # Verifica se o input consiste apenas em dígitos.
            if verificacao_int(deletar) == True:
                # Converte o input para inteiro.
                deletar = int(deletar)

                # Verifica se o ID existe no dicionário 'pacientes'.
                if deletar in pacientes.keys():
                    # Remove o paciente com o ID especificado.
                    del (pacientes[deletar])
                    print("Paciente deletado com sucesso")
                else:
                    # Se o ID não existe, exibe uma mensagem de erro.
                    print("Paciente inexistente")

                # Aguarda o usuário pressionar Enter para continuar.
                input("Pressione Enter para continuar")
                # Limpa a tela.
                print("\n" * 50)
            else:
                # Se o input não consiste apenas em dígitos, exibe uma mensagem de erro.
                print("Digitado uma letra, tente novamente")

                # Aguarda o usuário pressionar Enter para continuar.
                input("Pressione Enter para continuar")
                # Limpa a tela.
                print("\n" * 50)

        case 0:
            # Encerra o programa.
            print("Sistema encerrado")
            break

        case _:
            # Se o usuário digitar uma opção inválida, exibe uma mensagem de erro.
            print("Opção inválida")
          
