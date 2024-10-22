from modelos.restaurante import Restaurante

restaurante_praca = Restaurante(nome='Praça', categoria='Gourmet')
restaurante_mexicano = Restaurante(nome='Mexican Food', categoria='Mexicana')
restaurante_japones = Restaurante(nome='Japa', categoria='Japonesa')

restaurante_praca.receber_avaliacao()
restaurante_praca.receber_avaliacao()




restaurante_mexicano.alternar_estado()
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()