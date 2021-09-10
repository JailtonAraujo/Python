# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.19 Modifique o programa para aceitar valores decimais, ou seja, também contar moedas de 0,01, 0,02, 0,05, 0,10 e 0,50.

valor = float(input("Digite o valor a pagar:"))
cedulas= 0
apagar = valor
atual = 100

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        if atual >= 1:
            print(f"{cedulas} cedula(s) de R${atual}")
        else:
            print(f"{cedulas} moeda(s) de {atual:5.2f}")
        if apagar < 0.01:
            break
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        cedulas = 0

