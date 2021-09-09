# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.12 Altere o programa anterior de forma a perguntar também o valor 
# depositado mensalmente. Esse valor será depositado no início de cada mês, e você 
# deve considerá-lo para o cálculo de juros do mês seguinte. 

deposisto_inicial = float(input("Informe o deposito inicial:"))
taxa_de_juros = float(input("Informe a taxa de juros:"))


i = 1

while i <= 24:
    deposito_mensal = float(input("Informe o valor do deposito do {i}º mês:"))
    deposisto_inicial = deposito_mensal + deposisto_inicial + ((deposisto_inicial*taxa_de_juros)/100)
    print(f"{i}º mês {deposisto_inicial:5.2f}")
    i += 1
