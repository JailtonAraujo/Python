# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 7.4 Escreva um programa que leia uma string e imprima quantas vezes
#cada caractere aparece nessa string.

S1 = input("Digite uma String:")
cont = {}

for letra in S1:
    cont[letra ] = cont.get(letra, S1.count(letra))

for letra, num in cont.items():
    print(f"{letra} : {num}X")
