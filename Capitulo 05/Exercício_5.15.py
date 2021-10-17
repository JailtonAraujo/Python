# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.15 Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade 
# comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto:

# |Codigo|  Preço|
# |  1   |  0.50 |
# |  2   |  1.00 |
# |  3   |  4.00 |
# |  5   |  7.00 |
# |  9   |  8.00 |

#Seu programa deve exibir o total das compras depois que o usuário digitar O. 
#Qualquer outro código deve gerar a mensagem de erro "Código inválido''.


total = 0
entrada = 1

while entrada != 0:
    entrada = int(input("Digite o codigo do produto:"))
    if entrada == 1:
        total += 0.50
    elif entrada == 2:
        total += 1.00
    elif entrada == 3:
        total += 4.00
    elif entrada == 5:
        total += 7.00
    elif entrada == 9:
        total += 8.00
    elif entrada != 1 and entrada != 2 and entrada != 3 and entrada != 5 and entrada!= 9 and entrada != 0:
        print("Codigo invalido!")

print(f"O total das compras foi R${total}")
