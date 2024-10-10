def nome_programa():
    print("""Esse número é Par ou Impar
          """)
    
def solicitar_numero_usuario():
    try:
        numero = int(input('Digite um número: '))

        match numero % 2:
            case 0:
                print('Esse é um número par')
            case  1:
                print('Esse é um número impar')
    except ValueError:
        print('Por favor, digite um número válido')

def main():
    nome_programa()
    solicitar_numero_usuario()


if __name__ == '__main__':
    main()