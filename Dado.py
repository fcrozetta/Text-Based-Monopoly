from random import randint
def jogarDado():
    return randint(1, 6)  # Retorna um numero aleatorio entre 1 e 6

def dadosIguais(dados):
    dado = dados[0]
    if dados.count(dado) < len(dados):
        """se a quantidade de vezes que o valor da primeira posicao aparece for igual ao tamanho do vetor,
        entao todos os dados sao iguais!"""
        return False
    else:
        return True