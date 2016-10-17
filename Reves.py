import Configuracoes
from Dado import jogarDado
from random import randint

def gera_reves():
    if jogarDado() % 2 == 0:  # Joga o dado.. se for par eh sorte, se nao eh reves
        opcao = randint(0, (len(Configuracoes.possiveis_sorte) - 1))
        print("SORTE!")
        for key in Configuracoes.possiveis_sorte[opcao].keys():
            print(key)
        for value in Configuracoes.possiveis_sorte[opcao].values():
            print("+", value)
            return int(value)
    else:
        opcao = randint(0, (len(Configuracoes.possiveis_reves) - 1))
        print("REVES!")
        for key in Configuracoes.possiveis_reves[opcao].keys():
            print(key)
        for value in Configuracoes.possiveis_reves[opcao].values():
            print("-", value)
            return int(value) * -1
