'''
v = Array de valores
w = Array de pesos
W = Máximo de Kilos que se pode levar

n = Objetos
'''


def fractionalKnapsack(v, w, W):
    densitity = sorted(zip(v, w))

    for index, pair in enumerate(densitity):
        v[index] = pair[0]
        w[index] = pair[1]

    x = []

    for i in range(len(v)):
        x.append(0)

    i = 0
    while w[i] <= W:
        x[i] = 1
        W = W - w[i]
        i = i + 1

        ## valor maximo que i pode ir, é o tamanho maximo do vetor de valores ou pesos
        if i > len(v) - 1:
            i = len(v) - 1
            break


    if W > 0:
        x[i] = W / w[i]
    return x

#para retornar o valor correto: ex = 240.0
# v = [60,100]
# w = [10,20]
# result = fractionalKnapsack(v, w, W=50)
# final = float(0)
# for index, i in enumerate(result):
#     final += i * v[index]
# print(final)
