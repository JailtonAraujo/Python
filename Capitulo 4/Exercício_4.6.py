# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 4.6 Escreva um programa que pergunte a distância que um passageiro deseja  percorrer  em  km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até de 200km, e R$ 0,45 para viagens mais longas.

dist  = float(input("Qual a distância que voce deseja percorrer (Em km)?"))

if dist <= 200:
    print(f"O total a pagar é R${dist*0.50}")
else:
    print(f"O total a pagar é R${dist*0.45}")