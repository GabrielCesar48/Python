import os

restaurantes = [   {'nome' : 'Recanto Sabor de Minas',     'categoria' : 'Japonesa',       'ativo' : False}, 
                            {'nome' : 'Hazard Gourmet',                  'categoria' : 'Azerothiana',   'ativo' : True },
                            {'nome' : 'Zabawa',                                'categoria' : 'Brasileira',        'ativo' : True}]

def exibir_nome_programa():
    print('''Sabor Express

''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do Restaurante: ')
    categoria_restaurante = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')    
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo':False}    
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!' )
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Lista de Restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']

        print(f' - {nome_restaurante} | {categoria} | {ativo}')
    
    voltar_ao_menu()

def alternar_estado_restaurante():
     exibir_subtitulo('Alternando Estado do Restaurantes')
     nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
     for restaurante in restaurantes:
         if nome_restaurante == restaurante['nome']:
             restaurante_encontrado = True


     voltar_ao_menu()

def finalizar_app():
    exibir_subtitulo('App Finalizado')
    
def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu: ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def opcao_invalida():
    print('Opção inválida')
    voltar_ao_menu()

def escolher_opcao():

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
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()

