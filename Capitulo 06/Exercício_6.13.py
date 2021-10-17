# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 6.13 A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista
# T = [ -10, -8, 0, 1, 2, 5, -2, -4] . Faça um programa que imprima a menor e a
# maior temperatura, assim como a temperatura média.

T = [-10, -8, 0, 1, 2, 5, -2, -4]

menor = T[0]
maior = T[0]
soma = 0

for e in T:
    if e < menor:
        menor = e
    if e > maior:
       maior = e
    soma = soma + e

print(f"A menor temperatura é {menor}")
print(f"A maior temperatura é {maior}")
print(f"A temperatura media é {soma / len(T)}")



