# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.11 Escreva um programa que pergunte o depósito inicial e a taxa de 
# juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. 
# Escreva o total ganho com juros no período. 

deposisto_inicial = float(input("Informe o deposito inicial:"))
taxa_de_juros = float(input("Informe a taxa de juros:"))

i = 1

while i <= 24:
    deposisto_inicial = deposisto_inicial + ((deposisto_inicial*taxa_de_juros)/100)
    print(f"{i}º mês {deposisto_inicial:5.2f}")
    i += 1
