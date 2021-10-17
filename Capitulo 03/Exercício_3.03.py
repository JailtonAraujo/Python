# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 3.3 Complete a  tabela  a seguir utilizando a  = True, b  = False e c  = True.
# ----------------------------------------------------------------------------
# |Expressão|       Resultado       |       |Expressão|      Resultado     |
# |a and a  |  X  True  O  False    |       |a or c   |  X  True  O  False |
# |b end b  |  O  True  X  False    |       |b or c   |  X  True  O  False |
# |not c    |  O  True  X  False    |       |c or a   |  X  True  O  False |
# |not b    |  X  True  O  False    |       |c or b   |  X  True  O  False |
# |not a    |  O  True  X  False    |       |c or c   |  X  True  O  False |
# |a and b  |  O  True  X  False    |       |b or b   |  O  True  X  False |
# |b and c  |  O  True  X  False    |
# -----------------------------------------------------------------------------

a = True
b = False
c = True

print(a and a)
print(b and b)
print(not c)
print(not b)
print(not a)
print(a and b)
print(b and c)

print(20*"=")

print(a or c)
print(b or c)
print(c or a)
print(c or b)
print(c or c)
print(b or b)
