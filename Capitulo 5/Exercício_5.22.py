# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 5.22 Escreva um programa que exiba uma lista de opções (menu): adição,
#subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida.
#Repita até que a opção saída seja escolhida.


while True:
    print(30 * "=")
    print("{:^30}".format("TABUADA"))
    print(30*"=")
    print("[1] ADIÇÃO\n"
          "[2] SUBTRAÇÃO\n"
          "[3] DIVISÃO\n"
          "[4] MULTIPLICAÇÃO\n"
          "[5] PARA SAIR")
    opcao = int(input("ESCOLA UMA DAS OPÇÕES ACIMA\n>>>"))

    if opcao == 5:
        print("Finalizado com sucesso!")
        break
    elif opcao >= 1 and opcao < 5:
        num = int(input("Digite o numero para saber a tabuada:"))
        i =1

        if opcao == 1:
            while i <= 10:
                print(f"{num} + {i} = {num+i}")
                i += 1
        elif opcao == 2:
            while i <= 10:
                print(f"{num} - {i} = {num-i}")
                i += 1
        elif opcao == 3:
            while i <= 10:
                print(f"{num} ÷ {i} = {num/i:5.2f}")
                i += 1
        elif opcao == 4:
            while i <= 10:
                print(f"{num} X {i} = {num*i:5.2f}")
                i += 1
    else:
        print("Opção invalida!")