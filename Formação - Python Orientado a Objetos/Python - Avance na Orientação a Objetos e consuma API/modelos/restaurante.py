from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    """Representa um restaurante e suas características."""
    restaurantes = []
    
    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')
    
    @property 
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '☑' if self._ativo else '☐'
    
    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo
        
    def receber_avaliacao(self):  # Removi os parâmetros 'cliente' e 'nota'
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        cliente = input('Insira seu nome: ')        
    
    # Valida a nota até que seja um valor entre 0 e 5
        while True:
            try:
                nota = int(input('Deixe sua avaliação para o restaurante de 0 a 5: '))
                if 0 <= nota <= 5:
                    break
                else:
                    print('Valor inválido, insira uma avaliação de 0 a 5')
            except ValueError:
                print('Por favor, insira um número válido.')
        
        avaliacao = Avaliacao(cliente=cliente, nota=nota)
        self._avaliacao.append(avaliacao)
     
    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    def adicionar_no_cardapio(self, item):
        """
        Adiciona um item ao cardápio se for uma instância da classe ItemCardapio.

        Esta função verifica se o item fornecido é uma instância da classe ItemCardapio
        antes de adicioná-lo à lista de itens do cardápio.

        Parâmetros:
        item (ItemCardapio): O item a ser adicionado ao cardápio. Deve ser uma instância da classe ItemCardapio.

        Retorna:
        None
        """
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
            
    
    @property
    def exibir_cardapio(self):
        """
        Exibe o cardápio do restaurante, listando pratos e bebidas com suas respectivas informações.

        Esta propriedade imprime o cardápio do restaurante, mostrando o nome do restaurante e enumerando
        os itens disponíveis. Se o item tiver o atributo 'descricao', ele é tratado como um prato, e as
        informações de nome, preço e descrição são exibidas. Caso contrário, o item é tratado como uma bebida,
        e as informações de nome, preço e tamanho são exibidas.

        Não há parâmetros de entrada.

        Retorna:
        None (apenas exibe o cardápio no console).
        """
        print(f'Cardápio do restaurante {self._nome} \n')
    
        # Percorre os itens do cardápio e exibe suas informações
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):  # Verifica se o item é um prato
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:  # Se não tiver descrição, trata o item como bebida
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
