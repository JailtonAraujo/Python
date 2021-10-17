# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.5 Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.

i = 1

while i <= 10:
    if i % 3 == 0:
        print(i)
    i += 1