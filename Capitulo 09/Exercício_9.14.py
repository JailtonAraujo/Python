# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

import sys

#Exercício 9.14 Crie um programa que leia um arquivo-texto e elimine os espaços
#repetidos entre as palavras e no fim das linhas. O arquivo de saída também não
#deve ter mais de uma linha em branco repetida.

if len(sys.argv) != 3:
    print("\nUso: e09-14.py entrada saida\n\n\n")
    sys.exit(1)

entrada = sys.argv[1]
saida = sys.argv[2]

arquivo = open(entrada, "r", encoding="utf-8")
arq_saida = open(saida, "w", encoding="utf-8")
branco = 0

for linha in arquivo:
    # Elimina espaços a direita
    # Substitua por strip se também
    # quiser eliminar espaços a esquerda
    linha = linha.rstrip()
    linha = linha.replace("  ", "")  # Elimina espaços repetidos
    if linha == "":
        branco += 1  # Conta linhas em branco
    else:
        branco = 0   # Se a linha não está em branco, zera o contador
    if branco < 2:   # Não escreve a partir da segunda linha em branco
        arq_saida.write(linha+"\n")

arquivo.close()
arq_saida.close()