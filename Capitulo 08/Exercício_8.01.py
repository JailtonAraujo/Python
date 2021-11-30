# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 8.1 Escreva uma função que retorne o maior de dois números.
#Valores esperados:
#áxiMo(5, 6) == 6
#MáXÍM0(2, 1) == 2
#MáXlM0(7, 7) == 7

def maximo(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


num1 = int(input("Digite o Primeiro Numero:"))
num2 = int(input("Digite o Segundo Numero:"))

print( f"O Maior Numero é: {maximo(num1,num2)}")