# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 8.5 Reescreva a função do Programa 8.1 de forma a utilizar os métodos de
#pesquisa em lista, vistos no Capítulo 7.

Lista=[10,5,9,6,7,55,44]


def Pesquisar(lista, busca):
    x = 0
    while x < len(lista):
        if lista[x] == busca:
            return busca
            break
        x +=1
    return None

busca = int(input("Digite o Numero Que Deseja Buscar Na Lsita:"))

print(Pesquisar(Lista, busca))