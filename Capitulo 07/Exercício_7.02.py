# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 7.2 Escreva um programa que leia duas strings e gere uma terceira com
#os caracteres comuns às duas strings lidas.

S1 = input("Digite um texto:")
S2 = input("Digite outro texto:")
S3 = ""

for letra in S1:
    if letra in S2 and letra not in S3:
        S3 = S3 + letra
if S3 == "":
    print("As Strigs não tem caracteres em comum!")
else:
    print(f"Caracteres em comuns entre as strings: {S3}")