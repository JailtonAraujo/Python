# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 6.5 Altere o Programa 6.7 de forma a poder trabalhar com vários comandos digitados de uma só vez.
# Atualmente, apenas um comando pode ser inserido
# por vez. Altere-o de forma a considerar operação como uma string.

# Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos
# e, finalmente, a saída do programa.

ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar ultimo cliente ao final da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação = input("Operação (F, A ou S):")
    i = 0
    sair = False

    while i < len(operação):
        if operação[i] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} Atendido")
            else:
                print("Fila Vazia!")

        elif operação[i] == "F":
            ultimo += 1
            fila.append(ultimo)
        elif operação[i] == "S":
            sair = True
            break
        i += 1

    if sair == True:
        break








