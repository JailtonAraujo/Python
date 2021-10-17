# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 6.6 Modifique o programa para trabalhar com duas filas. Para facilitar
# seu trabalho, considere o comando A para atendimento da fila l; e B, para atendimento da fila 2.
# O mesmo para a chegada de clientes: F para fila l; e G, para fila 2.

ultimo = 10
fila1 = list(range(1, ultimo + 1))
fila2 = list(range(1, ultimo + 1))

while True:
    print(f"\nExistem {len(fila1)} clientes na fila")
    print(f"Fila 1 atual: {fila1}")
    print(f"Fila 2 atual: {fila1}")
    print("Digite F para adicionar ultimo cliente ao final da primeira fila\n"
          "Digite G para adicionar ultimo cliente ao final da segunda fila")
    print("Digite A para realizar o atendimento na primeira fila.\n"
          "Digite B para realizar o atendimento na segunda fila")
    print("Pressiona S para sair.")

    operação = input("Operação (F, G, A, B ou S):")
    i = 0
    sair = False

    while i < len(operação):
        #Atendimento na primeira fila
        if operação[i] == "A":
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f"Cliente {atendido} Atendido na primeira fila")
            else:
                print("Fila Vazia!")

        # Atendimento na segunda fila
        if operação[i] == "B":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} Atendido na segunda fila")
            else:
                print("Fila Vazia!")

        # Adicionando na primeira fila
        elif operação[i] == "F":
            ultimo += 1
            fila1.append(ultimo)

        #Adicionando na segunda fila
        elif operação[i] == "G":
            ultimo += 1
            fila2.append(ultimo)

        elif operação[i] == "S":
            sair = True
            break
        i += 1

    if sair == True:
        break
