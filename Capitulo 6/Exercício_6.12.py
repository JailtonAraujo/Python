# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 6.12 Altere o Programa 6.11 de forma a imprimir o menor elemento da lista.

L = [1, 7, 2, 4]
minimo = L[0]

for e in L:
    if e < minimo:
        minimo = e

print(f"O menor elemento da lista é {minimo}")
