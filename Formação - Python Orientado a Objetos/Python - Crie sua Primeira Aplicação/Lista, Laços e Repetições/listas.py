#1 - Crie uma lista para cada informação a seguir:

#Lista de números de 1 a 10;
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Lista com quatro nomes;
nomes = ['Gabriel', 'Cesar', 'Pereira', 'Crie']
#Lista com o ano que você nasceu e o ano atual.
anos = [1994, 2024]

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
valores = ['Gabriel', 48, 'Cesar', 1994, 'Pereira']
for valor in valores:
    print(valor)

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = 0
for numero in numeros:
    if numero % 2 == 1:
        soma_impares += numero
print(f'Soma de numeros ímpares de 0 a 10: {soma_impares}')

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente. 
numeros_decrescente = sorted(numeros, reverse=True)
for numero in numeros_decrescente:
    print(numero)

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
def tabuada():
    print('Tabuada do Número \n')
    numero_usuario = int(input('Digite um numero para saber sua tabuada: '))
    for i in range(1, 11):
        print(f'{numero_usuario} * {i} = {numero_usuario * i}')

tabuada()

#Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

lista_numeros = [1, 5, 15, 4, 'Gabriel', 6, 12, 5]
soma = 0
for numeros in lista_numeros:
    try:
        soma += numeros
    except TypeError:
        pass
print(f'Soma Total: {soma}')
        

lista_media = [5, 8, 32, 64, 1, 7, 0]
soma = 0

def media():




