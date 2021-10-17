# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.23 Escreva um programa que leia um número e verifique se é ou não
# um número primo. Para fazer essa verificação, calcule o resto da divisão do número
# por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma
# dessas divisões for igual a zero, o número não é primo. Observe que O e 1 não são
# primos e que 2 é o único número primo que é par.

num = int(input("Digte um numero:"))

if num < 0:
    print(f"{num} Numero invalido!")
if num == 0 or num ==1:
    print(f"Digite um maior que {num}")
else:
    if num == 2:
        print(f"{num} é um numero primo!")
    elif num % 2 == 0:
        print(f"{num} não é primo")
    else:
        cont = 3
        while cont < num:
            if num % cont == 0:
                break
            cont = cont + 2

        if cont == num:
            print(f"{num} É primo")
        else:
            print(f"{num} Não é primo!")