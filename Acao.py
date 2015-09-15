import Jogador, Terreno  # para teste apenas
import Reves
import Configuracoes
def verifica_terreno(jogador, terreno):
    if terreno.tipo == "propriedade":
        if terreno.proprietario is None:
            terreno_vazio(jogador, terreno)
        elif terreno.proprietario == jogador.nome:
            terreno_do_jogador(jogador, terreno)
        else:
            terreno_de_outro(jogador, terreno)
    elif terreno.tipo == "bloqueado":
        if terreno.nome == "Inicio":
            jogador.dinheiro += Configuracoes.dinheiro_inicial / 2
        elif terreno.nome == "Para Cadeia":
            prender(jogador)
    elif terreno.tipo == "reves":
        reves(jogador)


def terreno_do_jogador(jogador, terreno):
    print("Este Terreno eh seu!")
    print("\tNome: {nome}\n\tValor: {valor}\n\tAluguel: {aluguel}"
          "\n\tConsturcao: {construcao}\n\t".format(nome=terreno.nome, valor=terreno.valor, aluguel=terreno.aluguel,
                                                    construcao=Configuracoes.contrucoes[str(terreno.construcao)]
    ))

    if jogador.dinheiro >= terreno.aluguel and terreno.construcao < 3:
        opcao = input("Deseja Melhorar a construcao por {valor_upgrade}?(s/n)".format(valor_upgrade=terreno.aluguel))
        if opcao == "s":
            print("Melhoria realizada!")
            jogador.dinheiro -= terreno.aluguel
            terreno.construcao += 1


def terreno_vazio(jogador,terreno):
    print("O terreno {terreno_nome} esta a venda!\n\tValor: {terreno_valor}".format(
        terreno_nome=terreno.nome, terreno_valor=terreno.valor))
    if jogador.dinheiro >= terreno.valor:
        opcao = input("deseja Comprar?(s/n) ")
        if opcao == "s":
            print("{nome} comprou {terreno}".format(nome=jogador.nome, terreno=terreno.nome))
            jogador.comprar(terreno)
        else:
            print("{jogador} acha que o valor esta muito alto!".format(jogador=jogador.nome))
    else:
        print("Infelizmente voce nao tem dinheiro pra comprar.")

def terreno_de_outro(jogador, terreno):
    print("{terreno} Pertence a {outro_jogador}!\n\tAluguel: {aluguel}\nSuas Opcoes:".format(
        terreno=terreno.nome, outro_jogador=terreno.proprietario, aluguel=terreno.aluguel
    ))
    if jogador.dinheiro >= terreno.aluguel:
        print("\t1.Pagar Aluguel")
    print("\t0.Ir para cadeia")
    opcao = input("Sua escolha: ")
    if opcao == "0":
        prender(jogador)
    elif opcao == "1" and jogador.dinheiro >= terreno.aluguel:
        pagar_aluguel(jogador, terreno)


def prender(jogador):
    print("{jogador} foi PRESO".format(jogador=jogador.nome))
    jogador.posicao = Configuracoes.pos_Cadeia
    jogador.esta_preso = True

def buscar_proprietario(terreno):
    for jogador in Configuracoes.jogadores:
        if jogador.nome == terreno.proprietario:
            return jogador

def pagar_aluguel(jogador, terreno):
    print("Aluguel Pago!")
    jogador_proprietario = buscar_proprietario(terreno)
    jogador.dinheiro -= terreno.aluguel
    jogador_proprietario.dinheiro += terreno.aluguel

def reves(jogador):
    retorno_reves = Reves.gera_reves()
    jogador.dinheiro += retorno_reves

