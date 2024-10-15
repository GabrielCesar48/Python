# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro:
    def __init__(self, modelo='', cor='', ano=0000):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        
peugeout_208 = Carro('208', 'Cinza', '2024')

    
# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    def __init__(self, nome='', categoria='', ativo=False, prato_do_dia='', hora_abertura= 0):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.prato_do_dia = prato_do_dia
        self.hora_abertura= hora_abertura
        
zabawa = Restaurante(   nome='Zabawa', 
                                        categoria='Brasileira', 
                                        ativo=True, 
                                        prato_do_dia='Picanha', 
                                        hora_abertura=9)
        
    
 # Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
class Restaurante:
    def __init__(self, nome='', categoria='', ativo=False, prato_do_dia='', hora_abertura= 0):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.prato_do_dia = prato_do_dia
        self.hora_abertura= hora_abertura
        
santa_marmita = Restaurante(nome='Santa Marmita', categoria='Fast Food')
    
# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
class Restaurante:
    def __init__(self, nome='', categoria='', ativo=False, prato_do_dia='', hora_abertura= 0):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.prato_do_dia = prato_do_dia
        self.hora_abertura= hora_abertura
        
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
        

zabawa = Restaurante(   nome='Zabawa', 
                                        categoria='Brasileira', 
                                        ativo=True, 
                                        prato_do_dia='Picanha', 
                                        hora_abertura=9)

print(zabawa)



    
# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome='', idade=0, telefone='', cidade=''):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cidade=cidade

gabriel = Cliente(nome='Gabriel', idade=30, telefone='35988656135', cidade='Campos Gerais')
giovanna = Cliente(nome='Giovanna', idade=25, telefone='35992359888', cidade='Virginia')
mayara = Cliente(nome='Mayara', idade=30, telefone='35997334041', cidade='Jaguaribara')