import numpy as np
'''
    binaryKnapsack de acordo com o pseudocódigo.
'''
def binaryKnapsack(v, w, W):

    n = len(v)     
    K = np.zeros(shape=(n+1,W+1)) # instaciando matriz de zero's.

    for i in range(n + 1):
        for j in range(W+1):
            if w[i - 1] <= j:
                K[i][j] = max(v[i-1] + K[i-1][j - w[i - 1]], K[i-1][j])
            else:
                K[i][j] = K[i-1][j]
    return K
