# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Escreva um programa que leia duas strings e gere uma terceira, na
#qual os caracteres da segunda foram retirados da primeira.

S1 = input("Digite a primeira String:")
S2 = input("Digite a segunda String:")

S3 = ""

for letra in S1:
    if letra not in S2:
        S3 = S3 + letra

print(S3)