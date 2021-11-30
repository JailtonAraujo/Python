# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 8.7 Defina uma função recursiva que calcule o maior divisor comum
#(M.D.C.) entre dois números a e b, em que a> b.

def mdc(a,b):
    if a < b or b ==0:
        return a
    else:
        return mdc(a,b %b)

print(mdc(4,8))
