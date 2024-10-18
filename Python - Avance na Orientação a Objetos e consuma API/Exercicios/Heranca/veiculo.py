# Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.

class Veiculo:
    def __init__(self, marca='', modelo=''):
        self._marca = marca
        self.modelo = modelo
        self._ligado = False
        
# Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.

# Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro >>>>>>> continua no carro.py.
        
    def __str__(self):
        ligado_desligado = 'ligado' if self._ligado else "desligado"            
        return f'Marca: {self._marca} |  Modelo: {self.modelo} | Estado: {ligado_desligado}'
        
        
# peugeout_208 = Veiculo(marca='Peugeout', modelo='208')

# print(peugeout_208)