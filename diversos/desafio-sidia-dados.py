# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#quais os possiveis resultados dos dados esquecidos? (forgottenResults)

def solution(A, F, M):
    # write your code in Python 3.6
    resultsDice = A #array
    qtdForgottenResults = F #int
    arithmeticMean = M #int
    forgottenResults = [] #array possiveis resultados esquecidos
    media = 0
    lista = []
    num = 0

    while (media != lista):
        num += 1
        for i in range(1, qtdForgottenResults):
            forgottenResults.append(num)

        lista = forgottenResults + resultsDice
        media = sum(lista) / len(lista)
        if media == arithmeticMean:
            return forgottenResults
        forgottenResults = []

    #se o array não existe retorna [0]
    if len(forgottenResults) == 0:
        return [0]

    return forgottenResults
    pass
