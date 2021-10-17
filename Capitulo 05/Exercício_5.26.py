# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.26 Escreva um programa que calcule o resto da divisão inteira entre
# dois números. Utilize apenas as operações de soma e subtração para calcular o
# resultado.

num = float(input("Digite o primerio numero: "))
num2 = float(input("Digite o segundo numero:"))

i = num
resto = 0
while i >= num2:
    i = i - num2
resto = i;

print(f"O resto da divisão de {num} / {num2} é {resto}")