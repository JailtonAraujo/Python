# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 6.3 Faça um programa que percorra duas listas e gere uma terceira sem
# elementos repetidos.

lista1 = []
lista2 = []

#Preenchendo as listas#
while True:
    entrada = int(input("Digite um numero para inserir na primeira lista (Pressione 0 para terminar):"))
    if entrada ==0:
        break
    lista1.append(entrada)
while True:
    entrada = int(input("Digite um mumero para inserir na segunda lista (Pressione 0 para sair):"))
    if entrada == 0:
        break
    lista2.append(entrada)


lista3=[]
i=0

#Inserindo a primeira lista ba terceira e verificando se não tem elementos repetidos#
while i < len(lista1):
    j = 0
    while j < len(lista3):
        if lista1[i] == lista3[j]:
            break
        j+=1

    if j == len(lista3):
        lista3.append(lista1[i])
    i+=1
i=0

#Inserindo a segunda lista ba terceira e verificando se não tem elementos repetidos#
while i < len(lista2):
    j=0
    while j < len(lista3):
        if lista2[i] == lista3[j]:
            break
        j += 1

    if j == len(lista3):
        lista3.append(lista2[i])
    i +=1
i = 0


while i < len(lista3):
    print(f"{i} : {lista3[i]}")
    i+=1



