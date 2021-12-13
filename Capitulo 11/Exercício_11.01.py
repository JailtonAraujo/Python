# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 11.1 Faça um programa que crie o banco de dados preços.db com a tabela
#preços para armazenar uma lista de preços de venda de produtos. A tabela deve
#onter o nome do produto e seu respectivo preço. O programa também deve inserir
#alguns dados para teste.

import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('''
                create table preços(
                    nome text,
                    preço numeric)
                ''')
        cursor.execute('''
                insert into preços (nome, preço)
                    values(?, ?)
                    ''', ("Batata", "3.20"))
        cursor.execute('''
                insert into preços (nome, preço)
                    values(?, ?)
                    ''', ("Pão", "1.20"))
        cursor.execute('''
                insert into preços (nome, preço)
                    values(?, ?)
                    ''', ("Mamão", "2.14"))