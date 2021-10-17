# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 4.1 Analise o Programa 4.1. Responda o que acontece se o primeiro e o segundo valores forem iguais? Explique.

# se os valores forem iguais não acontecerá nada, por que nenhuma das condições foi cumprida, simplismente o programa vai encerrar!
#Vejamos!

a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))
if a > b:
    print(" O primeiro valor é o maior!")
if b > a:
    print("O segundo valor é o maior!")

