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
