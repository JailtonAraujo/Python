# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 3.9  Escreva  um programa que leia  a quantidade de dias, horas, minutos e segundos do  usuário. Calcule o  total  em  segundos.

dia = int(input("Digite a quantidade de dias:"))
hora = int(input("Digite a quantidade de horas:"))
minuto = int(input("Digite a quantidade de minutos:"))

print(f"{dia} dias + {hora} horas + {minuto} minutos equivalem {(dia * 86400) + (hora *3600) + (minuto * 60)} segundos")


