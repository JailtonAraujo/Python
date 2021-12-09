# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

import sys

#Exercício 9.1 Escreva um programa que receba o nome de um arquivo pela linha
#de comando e que imprima todas as linhas desse arquivo.

arquivo = open("arquivo.txt", "r")
for linha in arquivo.readlines():
    print(linha)
    arquivo.close()



