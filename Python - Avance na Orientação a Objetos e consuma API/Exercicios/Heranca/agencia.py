from Exercicios.banco import Banco

class Agencia(Banco):
    def __init__(self, nome='', endereco='', numero=0):
        super().__init__(nome, endereco)
        self._numero = numero