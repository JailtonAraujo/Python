# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.3 Faça um programa  para  escrever  a  contagem  regressiva  do  lança-mento de um foguete.
# O programa deve imprimir 10, 9, 8, ... , 1, O e Fogo! na tela.

num = 10

while num >= 0:
    print(f"{num}, ")
    num -= 1
print("FOGO!")