# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.4 Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.

fim = int(input("Digite o ultimo número a ser imprimido:"))
i = 0;

while i <= fim:
    if i % 2 == 1:
        print(i)
    i += 1 
