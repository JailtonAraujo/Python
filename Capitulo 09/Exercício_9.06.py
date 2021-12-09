# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 9.6 Modifique o Programa 9.5 para imprimir 40 vezes o símbolo de =
#se este for o primeiro caractere da linha. Adicione também a opção para parar de
#imprimir até que se pressione a tecla Enter cada vez que uma linha iniciar com .
#(ponto) como primeiro caractere.


LARGURA = 79
entrada = open("entrada.txt")
for linha in entrada.readlines():
    if linha[0] == ";":
        continue
    elif linha[0] == ">":
        print(linha[1:].rjust(LARGURA))
    elif linha[0] == "*":
        print(linha[1:].center(LARGURA))
    elif linha[0] == "=":
        print("=" * 40)
    elif linha[0] == ".":
        input("Digite algo para continuar")
        print()
    else:
        print(linha)
entrada.close()