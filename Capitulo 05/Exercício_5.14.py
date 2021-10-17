# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.14 Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite O (zero). No final da execução, 
# exiba a quantidade de números digitados, assim como a soma e a média aritmética. 

#entrada = float(input("Digite um numero:")) 
soma = 0
quant = 0
entrada = 1
while entrada != 0:
    entrada = float(input("Digite um numero:"))
    soma += entrada
    quant += 1
    
print(f"A soma de todos os numero digitados é: {soma}")
print(f"A quantidade de numero digitados é: {quant - 1}")
print(f"E a media aritmética é: {soma/(quant - 1)}")