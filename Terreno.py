class Terreno:
    def __init__(self, nome):
        self.nome = nome

    def propriedade(self, valor):
        """Define o terreno como Propriedade"""
        self.tipo = "propriedade"
        self.valor = valor
        self.construcao = 1
        self.aluguel = (self.valor /10 * self.construcao)
        self.proprietario = None

    def reves(self):
        self.nome = "Reves"
        self.tipo = "reves"

    def inicio_do_jogo(self):
        self.name = "Inicio"
        self.tipo = "bloqueado"

    def cadeia(self):
        self.name = "Cadeia"
        self.tipo = "bloqueado"

    def vai_cadeia(self):
        self.name = "Vai para cadeia"
        self.tipo = "bloqueado"
