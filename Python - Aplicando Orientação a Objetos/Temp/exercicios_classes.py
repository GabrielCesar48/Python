
    
    # código omitido

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_hazard_gourmet = Restaurante()
restaurante_hazard_gourmet.nome = 'Hazard Gourmet'
restaurante_hazard_gourmet.categoria = 'Gourmet'

restaurante_recanto_sabor_minas = Restaurante()
restaurante_recanto_sabor_minas.nome = 'Recanto Sabor de Minas'
restaurante_recanto_sabor_minas.categoria = 'Brasileira'

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurantes = [restaurante_hazard_gourmet, restaurante_recanto_sabor_minas, restaurante_praca]

print(vars(restaurante_praca))


    # Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
restaurante_praca.categoria = 'Italiana'
print(vars(restaurante_praca))
    
    # Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
nome_restaurante = restaurante_praca.nome
    
    # Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
status_restaurante = restaurante_praca.ativo

status = 'Ativo' if status_restaurante else 'Inativo'
print(status)
    # Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = restaurante_recanto_sabor_minas.categoria
print(categoria)
    
    # Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.nome = 'Bistrô'
print(restaurante_praca.nome)

    # Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza_place = Restaurante()
restaurante_pizza_place.nome = 'Pizza Place'
restaurante_pizza_place.categoria = 'Fast Food'

    # Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
restaurante_praca_categoria = restaurante_praca.categoria
print(restaurante_praca_categoria) 

    # Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza_place.ativo = True
    
    # Imprima no console o nome e a categoria da instância restaurante_praca.
restaurante_praca_nome_cat = [restaurante_praca.nome, restaurante_praca.categoria]
print(restaurante_praca_nome_cat)
                              
                              
                    



