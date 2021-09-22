# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 6.9 Modifique o exemplo para pesquisar dois valores. Em vez de apenas p,
# leia outro valor v que também será procurado. Na impressão, indique qual dos
# dois valores foi achado primeiro.

L = [15, 7, 27, 39]
p = int(input("Digite um valor a procurar: "))
v = int(input("Digite outro valor a ser procurado:"))
i = 0
j = 0
x = 0

posicao1 = len(L)
posicao2 = len(L)

while x < len(L) :
    if L[x] == p:
        i = 1
        posicao1 = x
    elif L[x] == v:
        j = 1
        posicao2 = x
    x += 1

if i == 1:
    if posicao1 < posicao2:
        print(f"{p} achado na posição {posicao1} primeiro!")
    else:
        print(f"{p} achado na posição {posicao1}")
elif i == 0:
    print(f"{p} não encontrado")

if j == 1:
    if posicao2 < posicao1:
        print(f"{v} achado na posição {posicao2} primeiro!")
    else:
        print(f"{v} achado na posição {posicao2}!")
elif j == 0:
    print(f"{v} não encontrado!")