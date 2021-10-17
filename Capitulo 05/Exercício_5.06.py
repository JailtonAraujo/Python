# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.6 Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2xl = 2, 2x2  = 4, ... 

num = int(input("Digite o numero que você deseja saber a tabuada:"))
i = 1

while i <= 10:
    print(f"{num} X {i} = {num * i}")
    i += 1