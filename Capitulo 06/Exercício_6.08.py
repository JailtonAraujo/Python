# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 6.8 Modifique o primeiro exemplo (Programa 6.9) de forma a realizar a
#mesma tarefa, mas sem utilizar a variável achou. Dica: observe a condição de saída
#do while.

L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
i = 0
x = 0

while x < len(L) :
    if L[x] == p:
        i = 1
    if i == 1:
        break
    x += 1

if i == 1:
    print(f"{p} achado na posição {x}")
elif i == 0:
    print(f"{p} não encontrado")