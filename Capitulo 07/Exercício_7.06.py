# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 7.6 Escreva um programa que leia três strings. Imprima o resultado da
#substituição na primeira, dos caracteres da segunda pelos da terceira.

S1 = input("Digite a primeira String:")
S2 = input("Digite a segunda String:")
S3 = input("Digite a terceira String:")

if len(S2) == len(S3):
    resultado = ""
    for letra in S1:
        posição = S2.find(letra)
        if posição != -1:
            resultado += S3[posição]
        else:
            resultado += letra

    if resultado == "":
        print("Todos os caracteres foram removidos.")
    else:
        print(f"Os caracteres {S2} foram substituidos por "
              f"{S3} em {S2}, gerando: {resultado}")
else:
    print("ERRO: A segunda e a terceira string devem ter o mesmo tamanho.")
