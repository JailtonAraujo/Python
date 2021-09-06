# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício4.10 Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. 
# Calcule o preço a pagar de acordo com a tabela a seguir.
# 
# tipo        | Faixa (KWh)   |  preço
# Residencial | Até 500       | R$ 0.40
#             | Acima de 500  | R$ 0.65
# Comércial   | Ate 1000      | R$ 0.55
#             | Acima de 1000 | R$ 0.60
# Industrial  | Até 5000      | R$ 0.55
#             | Acima de 5000 | R$ 0.60


print("Escola uma entra as instalações abaixo:\n[r] para residênciais\n[i] para industriais\n[c] para comércias")
tipo_de_instalacao = input(">>>")
print("\n")

if tipo_de_instalacao == "r":
    quant_kwh = float(input("Digite a quantidade de KWh consumidos:"))
    if quant_kwh <= 500:
        print(f"Seu consumo foi de {quant_kwh:5.2f}KWh e irá pagar um total de: R${(quant_kwh*0.40):5.2f}")
    elif quant_kwh > 500:
        print(f"Seu consumo foi de {quant_kwh:5.2f}KWh e irá pagar um total de: R${quant_kwh*0.65:5.2f}")

elif tipo_de_instalacao == "i":
    quant_kwh = float(input("Digite a quantidade de KWh consumidos:"))
    if quant_kwh <= 1000:
        print(f"Seu consumo foi de {quant_kwh:5.2f}KWh e irá pagar um total de: R${(quant_kwh*0.55):5.2f}")
    elif quant_kwh > 1000:
        print(f"Seu consumo foi de {quant_kwh:5.2f}KWh e irá pagar um total de: R${quant_kwh*0.60:5.2f}")

elif tipo_de_instalacao == "c":
    quant_kwh = float(input("Digite a quantidade de KWh consumidos:"))
    if quant_kwh <= 5000:
        print(f"Seu consumo foi de {quant_kwh:5.2f}KWh e irá pagar um total de: R${(quant_kwh*0.55):5.2f}")
    elif quant_kwh > 5000:
        print(f"Seu consumo foi de {quant_kwh:5.2f}KWh e irá pagar um total de: R${quant_kwh*0.60:5.2f}")

else: 
    print("Nemhuma opção valida foi selecionada!")

    

