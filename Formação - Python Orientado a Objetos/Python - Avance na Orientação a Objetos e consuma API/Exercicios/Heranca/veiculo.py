# # Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.

# class Veiculo:
#     def __init__(self, marca='', modelo=''):
#         self._marca = marca
#         self.modelo = modelo
#         self._ligado = False
        
# # Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.

# # Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro >>>>>>> continua no carro.py.
        
#     def __str__(self):
#         ligado_desligado = 'ligado' if self._ligado else "desligado"            
#         return f'Marca: {self._marca} |  Modelo: {self.modelo} | Estado: {ligado_desligado}'
        
        
# # peugeout_208 = Veiculo(marca='Peugeout', modelo='208')

# # print(peugeout_208)


#-------------------------------------------------- NOVO EXERCICIO APROVEITANDO CLASSE VEICULO ---------------------------------------
#Hora da prática: métodos especiais e atributos

'''    Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
    No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
    Crie uma nova classe chamada Carro que herda da classe Veiculo.
    No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
    Em um arquivo chamado main.py, importe a classe Carro.
    No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.'''
    
from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self, marca='', modelo=''):
        self._marca = marca
        self.modelo = modelo
        self._ligado = False
        
        
    def __str__(self):
        ligado_desligado = 'ligado' if self._ligado else "desligado"            
        return f'Marca: {self._marca} |  Modelo: {self.modelo} | Estado: {ligado_desligado}'
    
    @abstractmethod
    def ligar():
        pass
    