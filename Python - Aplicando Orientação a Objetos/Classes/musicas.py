# Em programação orientada a objetos (OO), uma classe é um modelo para criar objetos. Um objeto é uma instância específica de uma classe, e as classes são utilizadas para definir o comportamento e as propriedades compartilhadas por um grupo de objetos relacionados.

# Por exemplo, uma classe Música poderia ter 3 atributos (que trazem as características ou propriedades de um objeto):

# nome
# artista
# duracao
# COPIAR CÓDIGO
# Agora é sua vez! Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo..
class Musica:
    nome = ''
    artista = ''
    duracao = int
    
toda_forma_de_poder = Musica()   
toda_forma_de_poder.nome = 'Toda Forma de Poder'
toda_forma_de_poder.artista = 'Engenheiros do Hawaii'
toda_forma_de_poder.duracao = 213

cinza = Musica()
cinza.nome = 'Cinza'
cinza.artista = 'Engenheiros do Hawaii'
cinza.duracao = 242

piano_bar = Musica()
piano_bar.nome = 'Piano Bar'
piano_bar.artista = 'Engenheiros do Hawaii'
piano_bar.duracao = 200