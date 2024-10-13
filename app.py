import os

restaurantes = [   {'nome' : 'Recanto Sabor de Minas', 'categoria' : 'Japonesa', 'ativo' : False}, 
                            {'nome' : 'Hazard Gourmet', 'categoria' : 'Azerothiana', 'ativo' : True },
                            {'nome' : 'Zabawa', 'categoria' : 'Brasileira', 'ativo' : True}]

def exibir_nome_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print('''Sabor Express

''')

def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Altivar/Desativar restaurante')
    print('4. Sair \n')

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do Restaurante: ')
    categoria_restaurante = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')    
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo':False}    
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!' )
    voltar_ao_menu()

def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Lista de Restaurantes')
    print(f'{'Nome do restaurante'.ljust(33)} | {'Categoria'.ljust(30)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo ='Ativado' if restaurante['ativo'] else 'Desativado'

        print(f' - {nome_restaurante.ljust(30)} | {categoria.ljust(30)} | {ativo}')
    
    voltar_ao_menu()

def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alternando Estado do Restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')
    voltar_ao_menu()

def finalizar_app():
   ''' Exibe mensagem de finalização do aplicativo '''
   exibir_subtitulo('App Finalizado')
    
def voltar_ao_menu():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu: ')
    main()

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    Inputs:
    - texto: str - O texto do subtítulo 
    '''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção inválida')
    voltar_ao_menu()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma Opção: '))
        match opcao_escolhida:
                case 1:
                    cadastrar_novo_restaurante()
                case 2:
                    listar_restaurantes()
                case 3:
                    alternar_estado_restaurante()
                case 4:
                    finalizar_app()
                case _:
                    opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()

