
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

tentativa = input("Digite uma palavra:")
tentativas = 1

while chutes:
    if tentativa == inicializador['sorteada']:
        print("Parabéns!! Você acertou!! :)")
        break
    else:
        print(inidica_posicao(inicializador['sorteada'],tentativa))
        tentativa += 1


