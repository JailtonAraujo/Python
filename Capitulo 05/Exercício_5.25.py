# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.25 Escreva um programa que calcule a raiz quadrada de um número.
# Utilize o método de Newton para obter um resultado aproximado. Sendo n o
# número a obter a raiz quadrada, considere a base 6=2. Calcule p usando a fórmula
# p=(b+(n/6))/2. Agora, calcule o quadrado de p. A cada passo, faça b=p e recalcule
# p usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o
# quadrado de p for menor que 0,0001.

num = float(input("Digite o numero para saber sua raiz quadrada:"))

b = 2

while abs(num - (b * b)) > 0.00001:
    p = (b + (num / b)) / 2
    b = p
print(f"A raiz aproximada de {num} é {p:5.5f}")