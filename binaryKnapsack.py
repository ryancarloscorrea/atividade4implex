import numpy as np
def binaryKnapsack(v, w, W):
    n = len(v)     
    k = np.zeros(shape=(n+1,W+1))

    for i in range(n):
        k[i][0] = 0

    for j in range(1,W):
        k[0][j] = 0

    for i in range(1,n):
        for j in range(1,W):
            if j < w[i]:
                k[i][j] = k[i - 1][j]
            else:
                k[i][j] = max(k[i - 1][j], k[i - 1][j - w[i]] + v[i])
    return k

v = [60,100,120]
w = [10,20,70]
W = 50
result = binaryKnapsack(v, w, W)  
print (result)
# final = float(0)

# for index, i in enumerate(result):
#     final += i * v[index]
#     print(final)
#para retornar o valor correto: ex = 240.0
# v = [60,100]
# w = [10,20]
# result = fractionalKnapsack(v, w, W=50)
# final = float(0)
# for index, i in enumerate(result):
#     final += i * v[index]
# print(final)
