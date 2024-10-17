# Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
from modelos.exercicios04 import Livro

    # No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
    
harry_potter_01 = Livro(titulo='Harry Potter e a Pedra Fisolofal', autor='J.K. Rowling', ano_publicacao=1997)
harry_potter_02 = Livro(titulo='Harry Potter e a Câmara Secreta', autor='J.K. Rowling', ano_publicacao=1998)

harry_potter_01.emprestar_a_classe()
print(harry_potter_01._disponivel)
   
   
    # No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
    
ano_especifico = 1998
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(livros_disponiveis_ano)
    # Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.

