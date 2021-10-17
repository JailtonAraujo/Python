# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 6.20 Escreva um programa que compare duas listas. Considere a primeira
#lista como a versão inicial e a segunda como a versão após alterações. Utilizando
#operações com conjuntos, seu programa deverá imprimir a lista de modificações
#entre essas duas versões, listando:
#• os elementos que não mudaram
#• os novos elementos
#• os elementos que foram removidos

C1 = {1,5,4,3,7}
C2 = {8,9,0,5,3}

print(f"Elementos que não mudaram: {C1 & C2}")
print(f"Novos elementos:{C2 - C1}")
print(f"Elementos que foram removidos: {C1 - C2}")