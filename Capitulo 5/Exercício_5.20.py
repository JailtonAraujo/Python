# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.20 O que acontece se digitarmos 0,001 no programa anterior? Caso ele
# não funcione, altere-o de forma a corrigir o problema.

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
            print(f"{cedulas} moeda(s) de {atual}")
        if apagar < 0.001:
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
        elif atual <= 0.01:
            atual = 0.001
        cedulas = 0