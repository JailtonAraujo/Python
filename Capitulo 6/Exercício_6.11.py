# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 6.11 Modifique o Programa 6.6 usando for . Explique por que nem todos
# os whi le podem ser transformados em for .

L = []
while True:
    n = int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)

    x = 0


for e in L:
    print(f"{e}")

#  O ciclo de repetição for exige que seja passado uma lista que irá determiar o começo e fim do ciclo, inicialmente, baseado na mesmo, ou seja o for é util quando temos que percorrer
# uma lista de forma sequêncial, imprimir os elemtos por exemplo. O primeiro ciclo while do programa 6.6 é um bom exemplo onde não podemos utilizar o for
# pois não temos como passar uma lista para o ciclo sendo que a mesma ainda será preenchida. Ou seja o for se torna inviavel quando queremos preencher uma lista
# ou editar a mesma elemento a elemento.