# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 9.30 Modifique o Programa 9.8 para gerar uma lista html, usando os elementos ul e H . Todos os elementos da lista devem estar dentro do elemento ul, e
#cada item dentro de um elemento H. Exemplo:
#cul><li>IteM1</li><li>IteM2</li><li>IteM3</li></ul>V

filmes = {
     "drama": ["Cidadão Kane", "O Poderoso Chefão"],
     "comédia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"],
     "policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
     "guerra": ["Rambo", "Platoon", "Tora!Tora!Tora!"]}

pagina = open("filmes.html", "w", encoding="utf-8")
pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>
""")
for c, v in filmes.items():
    pagina.write(f"<h1>{c.capitalize()}</h1>")
    pagina.write("<ul>")
    for e in v:
        pagina.write(f"<li>{e}</li>")
    pagina.write("</ul>")
pagina.write("""
</body>
</html>
""")
pagina.close()
