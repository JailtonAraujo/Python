# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 6.16 Modifique o Programa 6.20 para ordenar a lista em ordem decrescente.
# L = [1, 2, 3, 4, 5] deve ser ordenada como L = [5, 4, 3, 2, 1].

L = [ 1, 2, 3, 4, 5]

fim = len(L)

while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] < L[x+1]: # Mudando o operador de condição de > para < a orndenação da lista passa a ser decrescente
            trocou = True
            temp = L[x]
            L[x] = L[x+1]
            L[x+1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in L:
    print(e)