# Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa:
    def __init__(self, nome='', idade=0, profissão=''):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissão.upper()
        
    def __str__(self):
        return f'{self.nome} tem {self.idade} anos e sua profissão é {self._profissao}'
    
    
        