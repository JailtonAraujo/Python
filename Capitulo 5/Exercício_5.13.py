# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.13 Escreva um programa que pergunte o valor inicial de uma dívida e 
# o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número 
# de meses para que a dívida seja paga, o total pago e o total de juros pago.

divida = float(input("Qual o valor da divida?"))
juro = float(input("Informe o juro mensal:"))
pagamento = float(input("Qual o valor de cada Prestação?"))
numero_parcelas = 0
total =0
total_juros = 0
restante = 0
while divida != 1 :
    if divida >= pagamento:
        divida = divida + ((divida*juro)/100)
        total = total + divida
        total_juros = total_juros + ((divida*juro)/100)
        divida = divida - pagamento
        numero_parcelas += 1
    
    # Assim que a divida se tornar menor que o pagamento divida = 1 e o programa finaliza, atribui o restante a varivel restante, se ouver, e imprime para o usuario#
    if divida < pagamento:
        restante = divida
        divida = 1

    # Condição que verifica se as condições de pagamento são viaveis, casa ocorra algum exemplo de pagamento que nunca sera quitado, EX: divida = 100, juro = 10 e pagamento = 10
    if numero_parcelas > 50:
        print("Este modo de pagamento é inviavel almento o valor do pagamneto por favor!")
        divida = 1  


print(f"Você pagará um total de R${total:5.2f}")
print(f"Você pagará um juro total de R${total_juros:5.2f}")
print(f"Esta dívida sera paga em {numero_parcelas} parcelas e uma ultima no valor de R${restante:5.2f}")