# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

dist = float(input("Digite a distância a ser percorrida (em quilometros):"))
vm = float(input("Digite a valocidade media (km/h):"))

print(f"A distância de {dist}Km a uma velocidade de {vm}km/h sera percorrida em {dist/vm:.2f}h")