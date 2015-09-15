import Configuracoes

class Jogador:
    def __init__(self, nome):
        self.nome = nome  # Nome do Jogador
        self.dinheiro = Configuracoes.dinheiro_inicial
        self.jogadas = 1  # Quantidade de jogadas
        self.propriedades = []  # Array contendo as propriedades do jogador
        self.posicao = 0  # Posicao no tabuleiro (0 eh a posicao inicial)
        self.dados_iguais = 0
        self.esta_preso = False  # Flag para verificar se o jogador esta preso ou nao

    def mostra_resumo(self):
        """Mostra o resumo do jogador na tela"""
        print("Jogador: {nome}\tcasa: {casa}\n\tDinheiro: {dinheiro}\n\tQtd. Propriedades: {propriedades}".format(
            nome=self.nome, casa=self.posicao, dinheiro=self.dinheiro, propriedades=len(self.propriedades)))
        if self.esta_preso:
            print("ESTA PRESO!")

    def inicia_turno(self):
        """Inicializa as configuracoes para o jogador"""
        if self.dinheiro <= 0:
            print("{nome} Perdeu o jogo, porque seu dinehiro esta negativo :(".format(
                nome=self.nome
            ))
        self.jogadas = Configuracoes.jogadas_default
        self.dados_iguais = 0
        self.mostra_resumo()

    def caminha(self, casas):
        """casas eh a quantidade de casas que o jogador deve caminhar"""
        if self.posicao + casas >= Configuracoes.tamanho_tabuleiro:
            self.posicao = (self.posicao + casas) - Configuracoes.tamanho_tabuleiro
        else:
            self.posicao += casas

    def comprar(self, terreno):
        self.dinheiro -= terreno.valor
        terreno.proprietario = self.nome
        self.propriedades.append(terreno.nome)


