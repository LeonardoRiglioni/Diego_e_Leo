# EX 1
def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_posiçao = []
    lista_posiçao.append([linha,coluna])
    i = 1
    while i < tamanho:
        if orientacao == "vertical":
            lista_posiçao.append([linha+i,coluna])
        elif orientacao =="horizontal":
            lista_posiçao.append([linha,coluna+i])
        i += 1
    return lista_posiçao

# EX 2 
def preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho):
    nova_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = []

    frota[nome_navio].append(nova_posicoes)

    return frota

# EX 3
def faz_jogada(tabuleiro, linha , coluna):
    if tabuleiro[linha][coluna]== 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

# EX 4

def posiciona_frota(frota):
    grid = []

    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        grid.append(linha)
    for tipo,lista in frota.items():
        for navio in lista:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                grid[linha][coluna] = 1

    return grid

# Ex 5 
def afundados(frota, tabuleiro):
    soma = 0
    for nomes in frota.values():
        for navio in nomes:
            n = 0
            for posicao in navio:
                if tabuleiro[posicao[0]][posicao[1]] == 'X':
                    n += 1
            if n >= len(navio):
                soma += 1 
    return soma

# Ex 6
def posicao_valida(frota,linha,coluna,orientacao,tamanho):
    posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    for coordenada in posicao:
        if coordenada[0] < 0 or coordenada[0] > 9 or coordenada[1] < 0 or coordenada[1] > 9:
          return False

    for tipo, navios in frota.items():
        for navio in navios:
            for ocupada in navio:
                if ocupada in posicao:
                    return False

    return True

# Ex 7
navios = ['porta-aviões','navio-tanque','contratorpedeiro','submarino']
tamanho = 4
frota = {}
while tamanho >= 1:
    for nome_navio in navios:
        print(f'Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}') 
        linha = int(input("Qual linha?"))
        coluna = int(input("Qual coluna?"))
        if tamanho > 1:
            orientaçao = int(input('1 ou 2?'))

        if posicao_valida(frota,linha,coluna,orientaçao,tamanho) == False:
            print('Esta posição não está válida!')
            linha = int(input("Qual linha?"))
            coluna = int(input("Qual coluna?"))
            if tamanho > 1:
                orientaçao = int(input('1 ou 2?'))
        else:
            preenche_frota(frota,nome_navio,linha,coluna,orientaçao,tamanho)[nome_navio] = define_posicoes(linha, coluna, orientaçao, tamanho)
        tamanho-= 1 
    print(preenche_frota)

