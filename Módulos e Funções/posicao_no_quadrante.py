import os

def finalizar_app():
    os.system('cls')
    print('Ponto fora do Quadrante\n')

def nome_programa():
    print('''Posição no Plano 
          ''')
def descrição_programa():
    print('Insira os valores de X e Y para determinar em qual quadrante do plano cartesiano o ponto se encontra')

def definir_posição():
    valor_x = float(input('Digite o valor de X: '))
    valor_y = float(input('Digite o valor de Y: '))

    if valor_x > 0 and valor_y > 0:
        print('Primeiro Quadrante')
    elif valor_x < 0 and valor_y > 0:
        print('Segundo Quadrante')
    elif valor_x < 0 and valor_y < 0:
        print('Terceiro Quadrante')
    elif valor_x > 0 and valor_y < 0:
        print('Quarto Quadrante')
    else:
        finalizar_app()

def main():
    nome_programa()
    descrição_programa()
    definir_posição()
    
if __name__ == '__main__':
    main()