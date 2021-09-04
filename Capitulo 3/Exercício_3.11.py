# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 3.11 Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.
valor = float(input("Digite o valor da mercadoria:"))
porcentagem = float(input("Digite o percentual de desconto:"))

print(f"O desconto da mercadoria é R${valor * porcentagem / 100} e o valor da mercadoria com o desconto aplicado custa: R${valor - (valor * porcentagem / 100)} ")