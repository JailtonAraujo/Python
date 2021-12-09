# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 9.29 Modifique o Programa 9.8 para utilizar o elemento p em vez de h2
#nos filmes.

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
    pagina.write(f"<h1>{c}</h1>")
    for e in v:
        pagina.write(f"<p>{e}</p>")
pagina.write("""
</body>
</html>
""")
pagina.close()