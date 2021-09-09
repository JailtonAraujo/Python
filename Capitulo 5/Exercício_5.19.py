# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.19 Modifique o programa para aceitar valores decimais, ou seja, também contar moedas de 0,01, 0,02, 0,05, 0,10 e 0,50. 

tabuada = 1 
while tabuada <= 10:  
    numero = 1 
    while numero <= 10:  
        print(f"{tabuada} x {numero} = {tabuada * numero}" ) 
        numero += 1
    tabuada+= 1  


