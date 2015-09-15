import os
import Configuracoes
from Jogador import Jogador
import Dado
import Tabuleiro
import Acao

def turno(jogador):
    os.system("clear")
    jogador.mostra_resumo()
    dados = []  # Array que contem os valores dos dados
    soma_dos_dados = 0
    jogador.jogadas -= 1  # Decrementa a quantidade de jogadas
    if jogador.esta_preso:
        print("{jogador} esta preso, e deve tirar valores iguais nos dados para sair!".format(jogador=jogador.nome))
    for dado in range(Configuracoes.quantidade_dados):
        dados.append(Dado.jogarDado())
    print("{jogador} jogou os dados e Conseguiu os seguintes numeros: ".format(jogador=jogador.nome), dados)

    if Dado.dadosIguais(dados):
        if jogador.dados_iguais == 3:
            Acao.prender(jogador)

        if jogador.esta_preso:
            print("Voce se Libertou!")
            jogador.esta_preso = False
        else:
            print("dados iguais, Uma nova jogada para {jogador}".format(jogador=jogador.nome))
            jogador.dados_iguais += 1  # Incrementa a quantidade de jogadas com dados iguais
            jogador.jogadas += 1  # Adiciona uma nova jogada para o jogador

    if not jogador.esta_preso:
        for dado in dados:
            soma_dos_dados += dado
        jogador.caminha(soma_dos_dados)

    # Carrega o objeto do terreno onde o jogador esta para a variavel casa
    casa = Tabuleiro.tabuleiro[jogador.posicao]
    Acao.verifica_terreno(jogador, casa)

    if jogador.jogadas == 0:
        print("Fim do turno do {jogador}.".format(jogador=jogador.nome))
    else:
        turno(jogador)


if __name__ == '__main__':

    for num_jogador in range(Configuracoes.quantidade_jogadores):
        nome = input("Digite o nome do jogador {num}: ".format(num=str(num_jogador)))  # Pega o nome do jogador
        jogador = Jogador(nome)  # Cria uma instancia do objeto para o jogador
        Configuracoes.jogadores.append(jogador)  # Adiciona o jogador na lista de jogadores

    while len(Configuracoes.jogadores) > 1:
        for jogador in Configuracoes.jogadores:
            jogador.inicia_turno()
            turno(jogador)
            input("Pressione qualquer tecla para continuar...")
