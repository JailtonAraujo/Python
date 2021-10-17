# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.9 Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. 
# Utilize apenas os operadores de soma e subtração para calcular o resultado. 
# Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo.
# Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo numero:"))
divisao = 0
i = num1

while (i != 0) or (i != 0):
    if i - num2 >= 0:
        divisao += 1 
        i = i - num2
    else:
        break


print(f"{num1} ÷ {num2} = {divisao}")
print(f"O resto da divisão de {num1} por {num2} = {i}")