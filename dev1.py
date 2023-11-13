import random
import string
from LISTA_PALAVRAS import *
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

def indica_posicao(sorteada, especulada):
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

print(" ===========================")
print("|                           |")
print("| Bem-vindo ao Insper Termo |")
print("|                           |")
print(" ==== Design de Software ===")
print("Comandos: desisto")
print("Regras:")
print("  - Você tem 6 tentativas para acertar uma palavra aleatória de 5 letras")
print("  - A cada tentativa, a palavra testada terá suas letras coloridas conforme:")
print("    Azul   : a letra está na posição correta;")
print("    Amarelo: a palavra tem a letra, mas está na posição errada;")
print("    Cinza: a palavra não tem a letra.")
print("  - Os acentos são ignorados;")
print("  - As palavras podem possuir letras repetidas.")
print("Sorteando uma palavra...")
print("Já tenho uma palavra! Tente adivinhá-la!")
print("Você tem 6 tentaviva(s)")
print("Qual seu palpite?")

chutes = True

filtro = filtra(PALAVRAS, 5)

inicializador = inicializa(filtro)

tentativas = 1

correta = inicializador['sorteada']

def verificacao(correta, tentativa):
    resultado = indica_posicao(correta, tentativa)
    ajuda = []
    for a, b in enumerate(resultado):
        if b == 0:
            ajuda.append('\033[34m' + tentativa[a]) 
        elif b == 1:
            ajuda.append('\033[33m' + tentativa[a])
        else:
            ajuda.append('\033[37m' + tentativa[a])
    return ' '.join(ajuda)

def jogo():
    while chutes == True and tentativas > 0 and tentativas <= 6:
        tentativa = input("Digite uma palavra:").lower()
        if tentativa == correta:
            print("Parabéns!! Você acertou!! :)")
            break
        if tentativa == 'desisto':
            print("A palavra correta era: {0}.".format(correta))
            break
        else:
            resultado = verificacao(correta, tentativa)
            print("Palavra errada. Dicas: {0}".format(resultado))
            tentativa += 1
