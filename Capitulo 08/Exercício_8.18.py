# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 8.17 Escreva um generator capaz de gerar a série de Fibonacci .

def fibonacci(n):
    p = 0
    s = 1
    while n > 0:
        yield p
        p, s = s, s + p
        n -= 1


for f in fibonacci(10):
    print(f)