# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 7.3 Escreva um programa que leia duas strings
# e gere uma terceira apenas com os caracteres que aparecem em uma delas.

S1 = input("Digite um texto:")
S2 = input("Digite outro texto:")
S3 = ""

for letra in S1:
    if letra not in S2 and letra not in S3:
        S3 = S3 + letra
for letra in S2:
    if letra not in S1 and letra not in S3:
        S3 = S3 + letra

if S3 == "":
    print("As Strings não possuem caracteres em comum!")
else:
    print(f"Caracteres que aparecem em uma delas: {S3}")