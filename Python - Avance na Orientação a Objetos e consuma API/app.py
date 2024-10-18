from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante(nome='Praça', categoria='Gourmet')
restaurante_mexicano = Restaurante(nome='Mexican Food', categoria='Mexicana')
restaurante_japones = Restaurante(nome='Japa', categoria='Japonesa')

bebida_suco = Bebida(nome='Suco de Melancia', preco=5.00, tamanho='grande')
prato_paozinho = Prato(nome='Paozinho', preco=2.00, descricao='O melhor pão da cidade')



restaurante_mexicano.alternar_estado()
def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()