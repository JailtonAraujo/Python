# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

import sys

#Exercício 9.9 Crie um programa que receba uma lista de nomes de arquivo e os
#imprima, um por um.

if len(sys.argv) < 2:
    print("\nUso: e09-09.py arquivo1 [arquivo2 arquivo3 arquivoN]\n\n\n")
    sys.exit(1)

for nome in sys.argv[1:]:
    arquivo = open(nome, "r")
    for linha in arquivo:
        print(linha, end="")
    arquivo.close()
