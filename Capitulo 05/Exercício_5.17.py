# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 5.17 O que acontece se digitarmos O (zero) no valor a pagar? 

valor = int(input(" Digite o valor a pagar:")) 
cedulas= 0 
atual = 50
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} cédula (s) de R${atual}")
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0

# Ao digitarmos 0 é escrito no console "0 cédula (s) de R$50", isso acontece pq a variavel atual inicia valendo 50 e como a digitarmos 0 
# a condição if não se cumpre e caimos no else e como a primeira instruçõe do bloco else é imprimir o numero de celulas e o valor da mesmo
# entende-se que ja que não teve nenhuma contagem de celulas e "atual" que inicia com 50 não teve alteração nos deparamos com esse resultado: "0 cédula (s) de R$50".

