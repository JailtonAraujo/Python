# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício4.9 Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.  
# O valor da prestação mensal não pode ser superior a 30% do salário. 
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar. 

valor_da_casa = float(input("Informe o valor da casa:"))
salario = float(input("Informe seu salário por favor:"))
quant_anos = float(input("Em quantos anos será divido o pagamento da casa?"))

valor_da_prestaca = valor_da_casa / (quant_anos * 12)

print(f"{valor_da_prestaca:5.2f}")

if valor_da_prestaca >= (salario*30/100):
    print(f"você irá pagar {quant_anos * 12:3.1f} X de R${valor_da_prestaca:5.2f} infelizmente não podemos aprovar sua compra, pois ela compromete mais que 30% do seu salario!")
elif valor_da_prestaca < (salario*30/100):
    print(f"você irá pagar {quant_anos * 12:3.1f} X de R${valor_da_prestaca:5.2f}, Parabéns, a compra da sua casa nova foi aprovada!")
