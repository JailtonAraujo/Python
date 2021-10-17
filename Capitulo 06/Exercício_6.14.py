# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#6.14 O que acontece quando a lista já está ordenada? Rastreie o Programa 6.20, mas com a lista L = [1, 2, 3, 4, S].


L = [ 1, 2, 3, 4, 5]

fim = 5

while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] > L[x+1]:
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


# Coso tente ordenar uma lista que ja esta ordenada o algoritmo ira percorrer a lista porem não fará alterações, pois a mesma já
# esta ordenada