# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 7.7 Modifique o o jogo da forca (Programa 7.2) de forma a escrever a
#palavra secreta caso o jogador perca.

palavra = input( "Digite a palavra secreta: ").lower().strip()

for x in range(100) :
    print()
digitadas = []
acertos= []
erros= 0

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou! ")
        break
    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra! ")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Vocé errou! ")
        print("X ==:==\nX : ")
        print("X O " if erros >= 1 else"X")
        linha2 = 1

