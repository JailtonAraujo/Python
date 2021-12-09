# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 9.7 Crie um programa que leia um arquivo-texto e gere um arquivo de
#saída paginado. Cada linha não deve conter mais de 76 caracteres. Cada página
#terá no máximo 60 linhas. Adicione na última linha de cada página o número da
#página atual e o nome do arquivo original.

LARGURA = 76
LINHAS = 60
NOME_DO_ARQUIVO = "mobydick.txt"


def verifica_pagina(arquivo, linha, pagina):
    if linha == LINHAS:
        rodapé = f"= {NOME_DO_ARQUIVO} - Página: {pagina} ="
        arquivo.write(rodapé.center(LARGURA - 1) + "\n")
        pagina += 1
        linha = 1
    return linha, pagina


def escreve(arquivo, linha, nlinhas, pagina):
    arquivo.write(linha + "\n")
    return verifica_pagina(arquivo, nlinhas + 1, pagina)


entrada = open(NOME_DO_ARQUIVO, encoding="utf-8")
saída = open("saida_paginada.txt", "w", encoding="utf-8")

pagina = 1
linhas = 1

for linha in entrada.readlines():
    palavras = linha.rstrip().split(" ")
    linha = ""
    for p in palavras:
        p = p.strip()
        if len(linha) + len(p) + 1 > LARGURA:
            linhas, pagina = escreve(saída, linha, linhas, pagina)
            linha = ""
        linha += p + " "
    if linha != "":
        linhas, pagina = escreve(saída, linha, linhas, pagina)

# Para imprimir o número na última página
while(linhas != 1):
    linhas, pagina = escreve(saída, "", linhas, pagina)

entrada.close()
saída.close()