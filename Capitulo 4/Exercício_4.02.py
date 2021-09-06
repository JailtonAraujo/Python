# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 4.2 Escreva um programa que pergunte a velocidade do carro de um usuário.
# Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado.
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80km/h .

vel = float(input("Qual sua velocidade (em km/h)?"))

if vel > 80:
    print(f"você ultrapassou o limite de velocidade de 80km/h e foi multado em: R${(vel - 80) * 5}")
if vel <= 80:
    print("Continue dirigindo com cuidado!")