# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 6.18 Escreva um programa que gere um dicionário, em que cada chave seja
#um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida.
#Exemplo: O rato -> {"O":1, "r":1, "a":1, "t":1, "o":1}

d = {}

for letra in "Orato":
    if letra in d:
        d[letra] = d[letra]
    else:
        d[letra] = 1

print(d)
