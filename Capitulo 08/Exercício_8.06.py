# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 8.6 Reescreva o Programa 8.2 de forma a utilizar for em vez de while

def soma(lista):
    total = 0
    for num in lista:
        total = total + num
    return total


Lista = [10, 5, 5]
print(soma(Lista))