# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 3.15 Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

quant_cigarros = int(input("Quantos cigarros você fuma por dia?"))
quant_anos = float(input("A quantos anos você é fumante?"))

print(f"Se você fuma {quant_cigarros} cigarros por dia e já é fumante a {quant_anos} anos, então você já perdeu "
      f"{((10 * quant_cigarros) * (quant_anos * 365)) // 1440} dias de vida!")