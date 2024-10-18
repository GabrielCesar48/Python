from veiculo import Veiculo

#Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.
class Carro(Veiculo):
    def __init__(self, marca='', modelo='', portas=0):
        super().__init__(marca, modelo)
        self._portas = portas
        
# Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.        
    def __str__(self):
        return f'{super().__str__()} | Portas: {self._portas}'
    
# Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual. >>>>> continua no moto.py