# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.24 Modifique o programa anterior de forma a ler um número n.
# Imprima os n primeiros números primos.

num = int(input("Digte um numero:"))

if num < 0:
    print(f"{num} Numero invalido!")
if num == 0 or num ==1:
    print(f"Digite um maior que {num}")
else:

    print(f"2")
    i = 1
    cont = 3
    while i <= num:
        n = 0
        j = 3
        if cont > num:
            break
        while j <= cont:
            if cont % j == 0:
                n = n + 1
            j = j + 1
        if n == 1:
            print(cont)
        cont = cont + 2
        i = i + 1

