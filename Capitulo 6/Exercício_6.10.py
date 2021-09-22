# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 6.10 Modifique o programa do Exercício 6.9 de forma a pesquisar p e v
# em toda a lista e informando o usuário a posição onde p e a posição onde v foram
# encontrados.


L = [15, 7, 27, 39]
p = int(input("Digite um valor a procurar: "))
v = int(input("Digite outro valor a ser procurado:"))
i = False
j = False
x = 0

posicao1 = len(L)
posicao2 = len(L)

while x < len(L) :
    if L[x] == p:
        i = True
        posicao1 = x
    elif L[x] == v:
        j = True
        posicao2 = x
    x += 1

if i == True:
        print(f"{p} achado na posição {posicao1}!")
elif i == False:
    print(f"{p} não encontrado")

if j == True:
        print(f"{v} achado na posição {posicao2}!")
elif j == False:
    print(f"{v} não encontrado!")