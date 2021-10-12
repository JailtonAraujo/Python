# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 6.15 O que acontece quando dois valores são iguais? Rastreie o Programa
# 6.20, mas com a lista L = [3, 3, 1, 5, 4].

L = [ 3, 3, 1, 5, 4]

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

# Quando submete uma lista com elemetos iguais no algoritmo ele ira ordenar a lista normalmente porém os elementos
# iguais serão postos em sequencia como este exmeplo.