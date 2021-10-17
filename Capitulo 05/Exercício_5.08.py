# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.8  Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. 
# Utilize apenas os operadores de soma e subtração para calcular o resultado. 
# Lembre-se de que podemos entender a multi-plicação de dois números como somas sucessivas de um deles. Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4. 

num1 = int(input("Digte o primeiro numero:"))
num2 = int(input("Digite o segundo número:"))

soma = 0
i = 1
while i <= num1 :
    soma  += num2
    i += 1
print(f"{num1} X {num2} = {soma} ")