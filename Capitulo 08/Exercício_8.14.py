import  random

# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 8.13 Altere o Programa 8.20 de forma que o usuário tenha três chances
#de acertar o número. O programa termina se o usuário acertar ou errar três vezes.

tentativas = 0;

num = random.randint(1, 10)
i =0
while(True):
    tentaiva = int(input("Escolha um numero entre 1 e 10:"))
    if(tentaiva == num):
        print("Parebéns, Você Acertou!")
        break
    else:
        tentativas +=1
        if(tentativas == 3):
            print("Que Pena Você Perdeu!")
            break
        print(f"Que Pena Você Erro, Ainda lhe Faltam {3 - tentativas}".format(tentativas))