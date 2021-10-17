# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 3.14 Escreva  um  programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km  rodado.

km = float(input("Digite a quantidade de quilometros percorridos:"))
dias = float(input("Digite a quantidade de dias o carro foi alugado?"))

print(f"Tendo o carro alugado por {dias} dias e percorrido {km}km o preço total do aluguel será: R${km * 0.15 + dias * 60}")