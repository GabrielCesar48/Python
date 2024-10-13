
def classificar_faixa():
    try:
        idade = int(input('Digite sua idade: '))
        
        if 0 < idade <= 12:
                print('Criança')
        if 12 < idade <= 18:
                print('Adolescente')
        if idade > 18:
                print('Adulto')
    except ValueError:
        print('Por favor, insira um numero válido')


def main():
    classificar_faixa()


if __name__ == '__main__':
    main()