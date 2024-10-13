import os

usuario = 'Gabriel.Pereira'
senha = '123@senha'

def finalizar_app():
    os.system('cls')
    print('Acesso Permitido\n')

def verificar_usuario():
    solicita_usuario = input('Digite seu usuário: ')
    solicita_senha = input('Digite sua senha: ')

    if solicita_usuario != usuario:
        print('Usuário Incorreto')
        verificar_usuario()
    elif solicita_senha != senha:
        print('Senha Incorreta')
        verificar_usuario()
    else:
        finalizar_app()

def main():
    verificar_usuario()
    
if __name__ == '__main__':
    main()