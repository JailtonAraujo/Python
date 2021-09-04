# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 3.13 Escreva um programa que converta uma temperatura digitada em ºC em ºF.
# A fórmula  para essa  conversão é: F = (9*C / 5) + 32

temp = float(input("Digite um temperatura em °C :"))

print(f"{temp}°C convertidos para ºF equivalem á: {(9*temp / 5) + 32}°F")