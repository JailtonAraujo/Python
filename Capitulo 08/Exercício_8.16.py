# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #


#Exercício 8.15 Utilizando a função type, escreva uma função recursiva que imprima
#os elementos de uma lista. Cada elemento deve ser impresso separadamente, um por
#linha.Considereocasodelistasdentrodelistas,comoL = [1, [2, 3, 4, [S, 6, 7]]].
#A cada nível, imprima a lista mais à direita, como fazemos ao indentar blocos em
#Python. Dica: envie o nível atual como parâmetro e utilize-o para calcular a quantidade de espaços em branco à esquerda de cada elemento.


ESPAÇOS_POR_NÍVEL = 4


def imprime_elementos(l, nivel=0):
    espacos = ' ' * ESPAÇOS_POR_NÍVEL * nivel
    if type(l) == list:
        print(espacos, "[")
        for e in l:
            imprime_elementos(e, nivel + 1)
        print(espacos, "]")
    else:
        print(espacos, l)


L = [1, [2, 3, 4, [5, 6, 7]]]

imprime_elementos(L)