# Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

# Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.
from carro import Carro
from moto import Moto

peugeout_208 = Carro(marca='Peugeout', modelo='208', cor='cinza')
onix = Carro(marca='Chevrolet', modelo='Onix', cor='azul')
fusca = Carro(marca='Volkswagem', modelo='Fusca', cor='branco' )

bros = Moto(marca='Honda', modelo='Bros', tipo='Casual')
cg150 = Moto(marca='Honda', modelo='CG150', tipo='Casual')
kawasaki = Moto(marca='Kawasaki', modelo='Ninja', tipo='Esportiva')

# Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.

print(peugeout_208)
print(onix)
print(fusca)

print(bros)
print(cg150)
print(kawasaki)
