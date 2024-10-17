    # Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
    
class Livro:
    livros = [] 
    def __init__(self, titulo = '', autor = '', ano_publicacao = 0):
        self._titulo = titulo.title()
        self._autor = autor.title()
        self._ano_publicacao = ano_publicacao
        self._disponivel = True  
        Livro.livros.append(self)  

    # Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    
    def __str__(self):
        return f'{self._titulo}, | Auror: {self._autor}, Ano de Publicação: {self._ano_publicacao}'

# print(harry_potter_01)
# print(harry_potter_02)

    # Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    def emprestar_a_classe(self):
        self._disponivel = False

        
# harry_potter_01 = livro(titulo='Harry Potter e a Pedra Fisolofal', autor='J.K. Rowling', ano_publicacao=1997)
# harry_potter_01.emprestar_a_classe()
# print(harry_potter_01._disponivel)   


    # Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano_especifico):
        livros_disponiveis = []
        for livro in Livro.livros:  # Acessa a lista de livros diretamente pela classe
            if livro._ano_publicacao == ano_especifico and livro._disponivel:
                livros_disponiveis.append(livro._titulo)
        return livros_disponiveis


# harry_potter_01 = Livro(titulo='Harry Potter e a Pedra Fisolofal', autor='J.K. Rowling', ano_publicacao=1997)
# harry_potter_02 = Livro(titulo='Harry Potter e a Câmara Secreta', autor='J.K. Rowling', ano_publicacao=1998)
    # Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
    

    # No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

    # No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

    # Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.
