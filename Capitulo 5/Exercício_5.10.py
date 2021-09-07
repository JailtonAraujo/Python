# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 5.10 Modifique o programa anterior para que aceite respostas com letras maiúsculas e minúsculas em todas as questões.

pontos = 0 
questão =  1 

while questão <= 3: 
    
    resposta=  input(f"Resposta da questão  {questão} : ") 
    if questão == 1 and resposta == "b" or resposta == "B":
        pontos = pontos + 1
    if questão == 2 and resposta == "a" or resposta == "A": 
        pontos = pontos + 1  
    if questão == 3 and resposta == "d" or resposta == "D": 
        pontos = pontos + 1

    questão = questão + 1

print(f"O aluno fez {pontos} ponto(s)")

