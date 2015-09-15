import Configuracoes
from Terreno import Terreno
from random import randint
tabuleiro = []

def cria_tabuleiro():
    for casa in range(Configuracoes.tamanho_tabuleiro):
        if casa == 0:
            terreno = Terreno("Inicio")
            terreno.inicio_do_jogo()
        elif casa == Configuracoes.pos_vai_para_cadeia:
            terreno = Terreno("Para Cadeia")
            terreno.vai_cadeia()
        elif casa == Configuracoes.pos_Cadeia:
            terreno = Terreno("Cadeia")
            terreno.cadeia()
        else:
            opcao = randint(0, 1)
            if opcao == 0:
                terreno = Terreno("Terreno {num}".format(num=casa))
                terreno.propriedade(randint(200,1500))
            else:
                terreno = Terreno("Reves")
                terreno.reves()
        tabuleiro.append(terreno)

cria_tabuleiro()
for casa in tabuleiro:
    print(casa.nome)