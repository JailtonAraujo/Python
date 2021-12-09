# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 10.1 Adicione os atributos tamanho e marca à classe Televisão. Crie dois
#objetos Televisão e atribua tamanhos e marcas diferentes. Depois, imprima o valor
#desses atributos de forma a confirmar a independência dos valores de cada instância (objeto).

class Televisao:
    def __init__(self):
        self.tamanho = ""
        self.marca = ""

tv1 = Televisao();
tv2 = Televisao();

tv1.tamanho = "32 polegadas"
tv1.marca = "tvsemp"
tv2.tamanho = "50 polegadas"
tv2.marca = "tvmais"

print(f"tamanho {tv1.tamanho} e marca {tv1.marca}")
print(f"tamanho {tv2.tamanho} e marca {tv2.marca}")

