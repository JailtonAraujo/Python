# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 6.1 Modifique o Programa 6.2 para ler 7 notas em vez de 5.

notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
i = 0

while i < 7:
    notas[i] = float(input(f"Nota {i}:"))
    soma += notas[i]
    i += 1
i = 0
while i < 7:
    print(f"Nota{i}: {notas[i]:5.2f}")
    i += 1

print(f"A media é {soma / i:5.2f}")
