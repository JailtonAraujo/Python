# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 3.10 Faça um  programa  que calcule o aumento de um salário.
# Ele  deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Digite seu salário:"))
porcentagem = float(input("Digite a porcentagem de aumento:"))

print(f"O salário no valor de R${salario} com um aumento de {porcentagem}% será equivalente á : R${(salario * porcentagem) / 100 + salario}")