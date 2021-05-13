from time import sleep


def formatar(info, moldura=0, texto=0, show=False):
    """
        ->Função que editará o texto passado e terá como elemento opcional cores:
        -> 0; Cor neutra, será usado quando o usuário não digitar nada ou o próprio 0
        -> 1; Cor vermelha
        -> 2; Cor verde
        -> 3; Cor amarela
        -> 4; Cor azul
    :param info: (OBRIGATÓRIO) Texto de entrada
    :param moldura: (OPCIONAL) cor que a linha terá
    :param texto: (OPCIONAL) cor que o texto terá
    :param show: (OPCIONAL) usado para enfeitar o programa
    :return: A frase passada no parâmetro "info"
    """
    sleep(0.5)
    cores = ['\033[m', '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m']
    tam = len(info) + 40
    if show:
        print(f'{cores[moldura]}-{cores[texto]}' * tam)
        print(str(info).center(tam))
        print(f'{cores[moldura]}-{cores[0]}' * tam)
    else:
        print(f'{cores[moldura]}-{cores[0]}' * tam)


def opcoes(moldura=0, texto=0):
    msg = 'MENU PRINCIPAL'
    formatar(msg, moldura=moldura, texto=texto, show=True)
    sleep(1)
    print(f'''1- Ver pessoas cadastradas
2- Cadastrar nova pessoa
3- Sair do programa''')
    while True:
        try:
            opcao = int(input('Escolha a sua opção: '))
            if opcao in [1, 2, 3]:
                break
        except ValueError:
            print(f'\033[1;31mERRO, por favor digite um número inteiro válido\033[m')
            continue
        else:
            print(f'\033[1;31mERRO, "\033[1;34m{opcao}\033[1;31m" não é um opção válida, tente novamente\033[m')
    formatar(msg, moldura=moldura, texto=texto)
    return opcao


def avaliar(moldura=0, texto=0):
    while True:
        escolha = opcoes(moldura, texto)
        if escolha == 1:
            try:
                arquivo = open('cadastros.txt', 'r')
            except FileNotFoundError:
                sleep(0.5)
                print('\033[1;32mAté o momento ninguém se cadastrou\033[m')
                sleep(1)
                print('\033[1;36mUm arquivo em branco foi criado\033[m')
                arquivo = open('cadastros.txt', 'a')
                arquivo.close()
            except Exception as erro:
                print(f'ERRO {erro.__class__} encontrado')
            else:
                while True:
                    linha = arquivo.readline().strip()
                    if linha == '':
                        arquivo.close()
                        break
                    print(linha)
        elif escolha == 2:
            arquivo = open('cadastros.txt', 'a')
            resp = validarnome()
            resp1 = f'{resp:<45}' + validaridade()
            arquivo.write(resp1 + ' anos\n')  # f'{resp:<25} anos\n'
            arquivo.close()
        else:
            print('Obrigado e tenha um bom dia!')
            break


def validarnome():
    while True:
        valido = False
        dado = str(input('Digite o nome: ')).strip().title()
        nome = dado.split()
        for pos, info in enumerate(nome):
            if not info.isalpha():
                print(f'\033[1;31mERRO, por favor digite um nome válido\033[m')
                break
            if pos == len(nome) - 1:
                valido = True
        if valido:
            break
    return dado


def validaridade():
    while True:
        try:
            while True:
                dado = int(input('Digite a idade: '))
                if dado > 0:
                    break
                else:
                    print('\033[1;31mERRO, por favor digite um idade válida\033[m')
        except ValueError:
            print(f'\033[1;31mERRO, digite uma idade válida\033[m')
        else:
            break
    return str(dado)
