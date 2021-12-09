# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #


#Exercício 8.13 Escreva uma função que receba uma string com as opções válidas
#a aceitar (cada opção é uma letra). Converta as opções válidas para letras minúsculas.
# Utilize input para ler uma opção, converter o valor para letras minúsculas
#e verificar se a opção é válida. Em caso de opção inválida, a função deve pedir ao
#usuário que digite novamente outra opção.

def Funcao(string):
    string.lower()
    while(True):
        letra = input("Digite a letra a procurar: ")
        letra.lower()

        if(letra in string):
            print("Achou")
            break
        else:
            while(True):

                letra = input("Errou! Digite Novamente: ")
                letra.lower()
                if(letra in string):
                    print("achou!")
                    break
            break



Funcao("jailton")
