# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 6.2 Faça um programa que leia duas listas e que gere uma terceira com os
# elementos das duas primeiras.

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]

lista3 = []

i = 0
# Passando o conteudo da lista1 para a lista3
while i < len(lista1):
    lista3.append(lista1[i])
    i+=1
i = 0

# passando o conteudo da lista2 para lista3
while i < len(lista2):
    lista3.append(lista2[i])
    i+=1

i =0
# Lendo o conteudo da lista3
while i < len(lista3):
    print(lista3[i])
    i+=1