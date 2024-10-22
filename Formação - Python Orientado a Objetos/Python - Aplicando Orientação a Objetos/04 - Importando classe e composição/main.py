# Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.

from modelos.exercicios04 import Livro

harry_potter_01 = Livro(titulo='Harry Potter e a Pedra Fisolofal', autor='J.K. Rowling', ano_publicacao=1997)
harry_potter_02 = Livro(titulo='Harry Potter e a Câmara Secreta', autor='J.K. Rowling', ano_publicacao=1998)

print(harry_potter_01)
print(harry_potter_02)