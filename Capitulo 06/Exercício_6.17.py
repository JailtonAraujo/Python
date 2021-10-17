# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

# Exercício 6.17 Altere o Programa 6.22 de forma a solicitar ao usuário o produto e a
# quantidade vendida. Verifique se o nome do produto digitado existe no dicionário,
# e só então efetue a baixa em estoque.



#print(tabela["Alface"])

#tabela["Alface"] = tabela["Alface"] + 2.50

#print(tabela["Alface"])

#while True:
 #   produto = input("Digite o nome do produto, digite 'fim' para sair:")
  #  if produto == "fim":
  #      break
   # if produto in tabela:
    #    print(f"Preço: {tabela[produto]}")
    #else:
     #   print("Produto não encontrado!")


estoque= {"tomate": [1000, 2.30],
"alface": [500, 0.45],
"batata": [2001, 1.20],
"feijão": [100, 1.50]}


produto = input("Digite o nome do produto:")
quantidade = int(input("Digite a quantidade:"))

venda = [[produto, quantidade]]

total= 0
print(f"Vendas:{venda}\n")

if produto in estoque:
    for operação in venda:
        produto, quantidade = operação
        preço = estoque[produto][1]
        custo = preço * quantidade
        print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
        estoque[produto][0] -= quantidade
        total += custo

    print(f" Custo total: {total:21.2f}\n")
    print("Estoque:\n")
    for chave, dados in estoque.items():
        print("Descrição: ", chave)
        print("Quantidade: ", dados[0])
        print(f"Preço: {dados[1]:6.2f}\n")
else:
    print("Produto não encontrado!")








