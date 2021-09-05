# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 4.5 Execute o  Programa 4.4 e experimente alguns valores. Verifique se os resultados foram os mesmos do Programa 4.2.

salario = float(input("Digite seu salario:"))

if salario > 1250:
    print (f"O seu salario atual é R${salario} com um aumento de 10% passou a ser {salario + (salario * 10 / 100)}")
else:
    print(f"O seu salario atual é R${salario} com um aumento de 15% passou a ser {salario + (salario * 15 / 100)}")

vel = float(input("Qual sua velocidade (em km/h)?"))

if vel > 80:
    print(f"você ultrapassou o limite de velocidade de 80km/h e foi multado em: R${(vel - 80) * 5}")
else:
    print("Continue dirigindo com cuidado!")