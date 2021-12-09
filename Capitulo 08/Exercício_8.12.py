# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 8.12 Escreva uma função que receba uma string e uma lista. A função
#deve comparar a string passada com os elementos da lista, também passada como
#parâmetro. Retorne verdadeiro se a string for encontrada dentro da lista, e falso,
#caso contrário.

def Buscar(string, lista):

        if(string in lista):
            return True
        else:
            return False

Lista = ["carlos", "silva", "abreu"]



print(Buscar("carlos", Lista))


