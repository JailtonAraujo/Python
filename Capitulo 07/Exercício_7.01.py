# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 7.1 Escreva um programa que leia duas strings. Verifique se a segunda
#ocorre dentro da primeira e imprima a posição de início.

S1 = input("Digite um texto:")
S2 = input("Digite outro texto:")

if S2 in S1:
    print("A segunda lista ocorre dentro da primeira!")
    print(f"A posição de inicio é: {S1.rfind(S2)}")

else:
    print("A segunda lista não ocorre dentro da primeira!")