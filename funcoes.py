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

