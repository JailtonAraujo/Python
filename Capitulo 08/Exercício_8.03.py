import math

# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 8.3 Escreva uma função que receba o lado de um quadrado e retorne sua
#área (A = lado2).
#Valores esperados:
#área_quadrado(4) == 16
#área_quadrado(9) == 81

def Area(lado):
    area = math.pow(lado,2)
    return area


lado = float(input("Digite o lado do quadrado que deseja saber a are:"))
print(Area(lado))