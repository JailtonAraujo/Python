# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 8.4 Escreva uma função que receba a base e a altura de um triângulo e
#retorne sua área (A= (base x altura) / 2).
#Valores esperados:
#área_triângulo(6, 9) == 27
#área_triângulo(5, 8) == 20

def Area(base, altura):
    area = (base*altura)/2
    return area

base = float(input("Digite a Base do Triângulo:"))
altura = float(input("Digite a Altura do Trangulo:"))

print(Area(base, altura))