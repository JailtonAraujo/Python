# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #


#Exercício 8.10 Reescreva a função para cálculo da sequência de Fibonacci, sem utilizar recursão.

def fatorial(n):
    i = 3
    t1 = 0
    t2 = 1
    soma = 0
    if n == 0 or n == 1:
        return 0
    else:
        print(f" {t1} ".format(t1),end='')
        print(f" {t2} ".format(t2), end='')
        while(i <= n):
            t3 = t1 + t2
            print(f" {t3} ".format(t3), end='')
            t1 = t2
            t2 = t3
            i += 1


print(fatorial(10))