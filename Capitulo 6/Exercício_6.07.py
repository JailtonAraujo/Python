# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 6.7 Faça um programa que leia uma expressão com parênteses. Usando
# pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
# Exemplo:

# ( ()) OK
# ()()(( )()) OK
# ()) Erro

# Você pode adicionar elementos à pilha sempre que encontrar abre parênteses e
# desempilhá-la a cada fecha parênteses. Ao desempilhar, verifique se o topo da pilha
# é um abre parênteses. Se a expressão estiver correta, sua pilha estará vazia no final.

sequencia = input("Digite a sequencia:")
i = 0
pilha=[]

while i < len(sequencia):
    if sequencia[i] == "(":
        pilha.append("(")
    if sequencia[i] == ")":
        if len(pilha) > 0:
            pilha.pop(-1)
        else:
            pilha.append(")")
            break
    i += 1

if len(pilha) == 0:
    print("OK!")
else:
    print("Erro!")
