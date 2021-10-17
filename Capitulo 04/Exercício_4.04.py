# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 4.4 Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input("Digite seu salario:"))

if salario > 1250:
    print (f"O seu salario atual é R${salario} com um aumento de 10% passou a ser {salario + (salario * 10 / 100)}")
if salario <= 1250:
    print(f"O seu salario atual é R${salario} com um aumento de 15% passou a ser {salario + (salario * 15 / 100)}")