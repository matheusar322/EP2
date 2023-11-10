import random
def filtra(lista, numero):
    lista_nova = []
    for palavra in lista:
        palavra_nova = palavra.lower()
        if len(palavra_nova) == numero and palavra_nova not in lista_nova:
            lista_nova.append(palavra_nova)
    return lista_nova


def inicializa(lista_palavras):
    dic = {}
    dic['n'] = len(lista_palavras[0])
    dic['sorteada'] = random.choice(lista_palavras)
    dic['especuladas'] = []
    dic['tentativas'] = len(lista_palavras[0]) + 1
    return dic

def inidica_posicao(sorteada, especulada):
    lista_posicao = []
    if len(sorteada) != len(especulada):
        return lista_posicao
    else:
        i = 0
        while i<len(sorteada):
            if especulada[i] in sorteada:
                if sorteada[i] == especulada[i]:
                    lista_posicao.append(0)
                else:
                    lista_posicao.append(1)
            else:
                lista_posicao.append(2)
            i += 1
    return lista_posicao