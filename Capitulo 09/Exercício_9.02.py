# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #
import sys

#Exercício 9.2 Modifique o programa do Exercício 9.1 para que receba mais dois
#parâmetros: a linha de início e a de fim para impressão. O programa deve imprimir
#apenas as linhas entre esses dois valores (incluindo as linhas de início e fim).

if len(sys.argv) != 4:  # Lembre-se que o nome do programa é o primeiro da lista
    print("\narquivo.txt\n\n")
else:
    nome = sys.argv[1]
    inicio = int(sys.argv[2])
    fim = int(sys.argv[3])
    arquivo = open("arquivo.txt", "r")
    for linha in arquivo.readlines()[inicio-1:fim]:
        # Como a linha termina com ENTER,
        # retiramos o último caractere antes de imprimir
        print(linha[:-1])
    arquivo.close()