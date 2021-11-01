import numpy as np
def binaryKnapsack(v, w, W):
    n = len(v)     
    k = np.zeros(shape=(n+1,W+1)) 

    for i in range(1,n):
        for j in range(1,W):
            if j < w[i]:
                k[i][j] = k[i - 1][j]
            else:
                k[i,j] = max(v[i] +k[i-1][j],k[i-1][j-w[i]] )
    print(  sum(w))
    return  k[i,j] 

v = [60,100,100,120]
w = [10,10,20,30]
W = 85
result = binaryKnapsack(v, w, W)  
print (result)
 
