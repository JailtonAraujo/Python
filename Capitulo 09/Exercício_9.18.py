# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 9.18 O que acontece se nome ou telefone contiverem o caractere usado
#como separador em seus conteúdos? Explique o problema e proponha uma solução.

# Se o # aparecer no nome ou telefone de uma entrada na agenda,
# ocorrerá um erro ao ler o arquivo.
# Este erro ocorre pois o número de campos esperados na linha será diferente
# de 2 (nome e telefone).
# O programa não tem como saber que o caracter faz parte de um campo ou de outro.
# Uma solução para este problema é substituir o # dentro de um campo antes de salvá-lo.
# Desta forma, o separador de campos no arquivo não seria confundido com o conteúdo.
# Durante a leitura a substituição tem que ser revertida, de forma a obter o mesmo conteúdo.