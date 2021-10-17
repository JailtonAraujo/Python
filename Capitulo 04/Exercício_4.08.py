# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.


print("ESCOLA UMA DAS OPÇÕES ABAIXO!")
print(30*"=")
print("DIGITE [1] PARA MULTIPLICAR\nDIGITE [2] PARA DIVIDIR\nDIGITE [3] PARA SOMAR\nDIGITE [4] PARA SUBTRAIR")
operacao = int(input(">>>"))

num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))

if operacao == 1:
    print(f"{num1} X {num2} = {num1*num2:5.2f}")
elif operacao == 2:
    print(f"{num1} ÷ {num2} = {num1/num2:5.2f}")
elif operacao == 3:
    print(f"{num1} + {num2} = {num1+num2:5.2f}")
elif operacao == 4:
    print(f"{num1} - {num2} = {num1-num2:5.2f}")

