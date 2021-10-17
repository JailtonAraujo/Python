# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.7 Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.

num = int(input("Digite o numero que você deseja saber a tabuada:"))

inicio = int(input("Digte o inicio da tabuada:"))
fim = int(input("Digite o fim da tabuada:"))

while inicio <= fim:
    print(f"{num} X {inicio} = {num * inicio}")
    inicio += 1



