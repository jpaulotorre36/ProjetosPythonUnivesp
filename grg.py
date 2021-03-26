tam = 3

def transposta(mat, ordem):
    transposta = criaMatriz(ordem, ordem)
    for i in range(tam):
        for j in range(tam):
            transposta[i][j] = mA[j][i]
    return transposta

    

mA = [[1,2], [3,4], [4,5]]
