#Arquivo que contem os parametros do jogo

quantidade_jogadores = 2 #quantidade de Jogadores
jogadores = [] #array que contem os jogadores(na ordem de jogo)
tamanho_tabuleiro = 40 #tamanho do array do tabuleiro (sempre multiplo de 4 para o tabuleiro ficar quadrado)
quantidade_dados = 2 #quantos dados serao usados
quantidade_reves = int(tamanho_tabuleiro/5) #quantos Sorte/Reves existirao no tabuleiro

dinheiro_inicial = 10000000 #dinheiro inicial de cada Jogador
jogadas_default = 1 #quantidade de Jogadas que cada jogador possui(pode alterarse dados forem iguais)

#cadeia e vai para cadeia devem ficar em cantos opostos do tabuleiro. Dividimos o tabuleiro em 4,
# e colocamos o vai para cadeia na primeira "esquina", e a cadeia na terceira esquina
pos_vai_para_cadeia = int(tamanho_tabuleiro/4) #Posicao da casa "vai para cadeia"
pos_Cadeia = int(pos_vai_para_cadeia * 3) #posicao da casa "cadeia"

contrucoes={
    '1': 'Nada',
    '2': 'Casa',
    '3': 'Hotel'
}

possiveis_sorte = [
    {"Ganhou na loteria!": "500"},
    {"Foi promovido no emprego!": "1500"}
]

possiveis_reves = [
    {"Perdeu o mindinho da mao esquerda": "500"},
    {"Seu filho pegou Piolho": "50"},
    {"Policia Apreendeu seus 15 hectares de maconha, por pouco nao foi preso!": "3500"}
]