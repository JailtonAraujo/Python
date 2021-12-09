# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

import os.path

#Exercício 9.31 Crie um programa que corrija o Programa 9.9 de forma a verificar se
#z existe e é um diretório.


if os.path.isdir("z"):
    print("O diretório z existe.")
elif os.path.isfile("z"):
    print("z existe, mas é um arquivo e não um diretório.")
else:
    print("O diretório z não existe.")