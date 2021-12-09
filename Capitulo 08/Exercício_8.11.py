# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #


#Exercício 8.11 Escreva uma função para validar uma variável string. Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres.
#Retorne verdadeiro se o tamanho da string estiver entre os valores de máximo e
#mínimo, e falso, caso contrário.

def validar(string, nummin, nummax):
    if(len(string) > nummin and len(string) < nummax):
        return True
    else:
        return False





print(validar("jailton", 6, 8))