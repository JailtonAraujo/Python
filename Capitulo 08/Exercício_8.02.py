# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 8.2 Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.
#Valores esperados:
#Múltiplo(8, 4) == True
#Múltiplo(5, 3) == False
#Múltiplo(5, 5) == True

def Multiplo(num1, num2):
    if num1 % num2 == 0:
        return True;
    else:
        return False;

num1 = int(input("Digite o Primeiro Numero:"))
num2 = int(input("Digite o Segundo Numero:"))

print(Multiplo(num1,num2))