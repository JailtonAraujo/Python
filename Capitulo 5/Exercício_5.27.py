# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 5.27 Escreva um programa que verifique se um número é palíndromo.
#Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
#Exemplos: 454, 10501

numero = input("Digite o numero(Sem espaços):")

i = 0

j = len(numero)-1

while j > i and numero[i] == numero[j]:
    j = j - 1
    i = i + 1

if numero[i] == numero[j]:
    print(f"{numero} é palindromo!")
else:
    print(f"{numero} não é palindromo!")


