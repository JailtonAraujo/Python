# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 4.3 Escreva um programa que leia três números e que imprima o maior e o menor.

num_1 = int(input("Digite o premeiro numero:"))
num_2 = int(input("Digite o segundo numero:"))
num_3 = int(input("Digite o terceiro numero:"))

if num_1 > num_2 and num_1 > num_3:
    print ("O primerio numero é o meior!")
if num_1 < num_2 and num_1 < num_3:
    print ("O primeiro numero é o menor!")

if num_2 > num_1 and num_2 > num_3:
    print ("O segundo numero éo maior!")
if num_2 < num_1 and num_2 < num_3:
    print ("O segundo numero é o menor!")

if num_3 > num_2 and num_3 > num_1:
    print ("O terceiro numero é o maior!")
if num_3 < num_2 and num_3 < num_1:
    print ("O terceiro numero é o menor!")
