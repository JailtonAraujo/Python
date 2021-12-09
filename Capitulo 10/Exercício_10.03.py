# coding=utf-8
# Exercícios do livro Introdução à Programação Com Python - 3° Edição
# Autor: Nilo Ney Coutinho Menezes
# Ano: 2019
# Editora: Novatec Editora Ldta #

#Exercício 10.3 Modifique a classe Televi.são de forma que, se pedirmos para mudar
#o canal para baixo, além do mínimo, ela vá para o canal máximo. Se mudarmos
#para cima, além do canal máximo, que volte ao canal mínimo. Exemplo:
#>>> tv = Televi.são( 2, 10)
#>>> tv .Muda_canal_para_bai.xo()
#»> tv.canal
#10
#>>> tv.Muda_canal_para_ci.Ma()
#»> tv.canal
#2


class Televisão:
    def __init__(self, min, max):
        self.ligada = False
        self.canal = min
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal-1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        if self.canal+1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin


tv = Televisão(2, 10)
tv.muda_canal_para_baixo()
print(tv.canal)
tv.muda_canal_para_cima()
print(tv.canal)