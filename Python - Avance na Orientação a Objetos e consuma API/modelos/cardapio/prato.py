from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome='', preco=0.00, descricao=''):
        super().__init__(nome, preco)
        self._descricao = descricao
        
        