# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #


# Exercício 4.7 Rastreie o Programa 4.6. Compare seu resultado ao apresentado na Tabela 4.2.

categoria = int(input("Digite a categoria do produto:"))

if categoria == 1:
    preco=10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    print("Categoria invalida, digite um valor entre 1 e 5!")
                    preco = 0;
print(f"P preço do produto é: R${preco:6.2f}")

# Este metodo de verificação tem mais desempenho do que so usando ifs normais, nesse caso assim que a condição é cumprida
# o restante das instruções são ignoradas. Porém devido aos deslocamentos das instruções o codigo fica um pouco confuso de entender.

