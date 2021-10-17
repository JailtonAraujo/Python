# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 6.19 Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
#   • os valores comuns às duas listas
#   • os valores que só existem na primeira
#   • os valores que existem apenas na segunda
#   • uma lista com os elementos não repetidos das duas listas.
#   • a primeira lista sem os elementos repetidos na segunda

L1 = {5,0,8,3,8,5}
L2 = {5,7,2,8,9,0,2}

print(f"Valores comuns às duas listas:{L1 & L2}")

print(f"Valores que só existem na primeira lista: {L1 - L2}")

print(f"valores que existem apenas na segunda lista: {L2 - L1}")


print(f"Elementos não repetidos das duas listas: {L1 ^ L2}")

print(f"Primeira lista sem os elementos repetidos na segunda: {L1 - L2}")
