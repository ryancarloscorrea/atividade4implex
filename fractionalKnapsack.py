'''
    fractionalKnapsack de acordo com o pseudocódigo.
'''

def fractionalKnapsack(v, w, W):

    densitity = sorted(zip(w, v), key=lambda x: - x[1]/x[0])

    for index, pair in enumerate(densitity):
        w[index] = pair[0]
        v[index] = pair[1]

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

#
# w = [ 7,  8, 14, 11,  3,  3,  9,  9,  3,10,  1, 12, 11,  1,  8,  9,  1,  6,  9, 13,  8,  1]
# v = [351, 195, 144, 603,  35, 435,  54, 269, 645, 235, 858, 273, 786, 809, 236, 670, 983, 643, 264, 130,190, 264]
# W = 10
# result = fractionalKnapsack(v, w, W)
# final = float(0)
# for index, i in enumerate(result):
#     final += i * v[index]
# print(final)
