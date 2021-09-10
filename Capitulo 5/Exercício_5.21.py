# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.21 Reescreva o Programa 5.1 de forma a continuar executando até que o
# valor digitado seja O. Utilize repetições aninhadas.
valor = 1
cedulas = 0
atual = 100
apagar = valor

while True:
    valor = float(input("Digite o valor a ser pago:"))
    apagar = valor
    atual = 100
    cedulas = 0
    if valor == 0:
        print("Finalizado com sucesso!")
        break
    while True:
        if atual <= apagar:
            apagar -= atual
            cedulas += 1
        else:
            print(f"{cedulas} cédula (s) de R${atual}")
            if apagar == 0:
                break
            if atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            cedulas = 0