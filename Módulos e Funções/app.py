import os

restaurantes = ['Recanto Sabor de Minas', 'Hazard Gourmet']

def exibir_nome_programa():
    print('''Sabor Express

''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o App\n')

def opcao_invalida():
    print('Opção inválida')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastramento de Restaurantes\n')
    nome_restaurante = input('Digite o nome do Restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!' )
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def escolher_opcao():

    try:
        opcao_escolhida = int(input('Escolha uma Opção: '))            
        match opcao_escolhida:
                case 1:
                    cadastrar_novo_restaurante()
                case 2:
                    print('Listar restaurantes')
                case 3:
                    print('Ativar restaurante')
                case 4:
                    finalizar_app()
                case _:
                    opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()