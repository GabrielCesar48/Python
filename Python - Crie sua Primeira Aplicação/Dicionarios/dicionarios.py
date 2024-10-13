#1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoa = {
    'nome':    'Gabriel', 
    'idade':    29, 
    'cidade':   'Varginha'
    }


#2 - Utilizando o dicionário criado no item 1:
#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
pessoa['idade'] = 30
print(pessoa)

#Adicione um campo de profissão para essa pessoa;
pessoa['profissão'] = 'Desenvolvedor de B.I.'
print(pessoa)

#Remova um item do dicionário.
profissao_removida = pessoa.pop('profissão')
print(pessoa)
print(profissao_removida)

# Remoção de Elemento
#del pessoa['cidade']

#3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

## Compressao de Dicionario
# quadrados = {num: num**2 for num in range(1,6)}
# print(quadrados)

#Loop Tradicional
quadrados = {}
for num in range(1,6):
    quadrados[num] = num**2

print(quadrados)

#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
pessoa2 = {
    'nome':    'Mislene', 
    'idade':    '25', 
    'cidade':   'Campos Gerais'
    }

tem_profissao = 'Possui' if 'profissao' in pessoa2  else 'Não possui'
print(tem_profissao)

#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
