import math
import numpy as np
import pandas as pd
import timeit
from fractionalKnapsack import fractionalKnapsack
from graph import generateGraph

'''
    primeira coluna da tabela é referente ao W
'''
if __name__ == '__main__':
    '''
    usar abaixo para o grafico
    '''
    # testTabelaDeTempos = []
    # testTableNitemsPorPeso = []
    # testTableResultadosSolFrac = []

    linha = 0
    indexTable = []
    column = ["W", 'n', 'frac', 'tf']

    minW= int(input('Digite o valor minimo da capacidade da mochila:'))
    maxW = int(input('Digite o valor maximo de items:'))
    stepW = int(input('Digite o intervalo do numero de items:'))

    pesos = []
    temposMochilaFracionaria = []

    while minW <= maxW:
        pesos.append(minW)
        minW += stepW


    # construindo base da tabela;
    for W in pesos:
        n = math.floor(W / 2)
        while n <= W * 2:
            indexTable.append(W)
            n += 5

    table = pd.DataFrame(columns=column, index=range(0, len(indexTable)))

    for W in pesos:
        n = math.floor(W / 2)

        while n <= W * 2:
            table.at[linha, "W"] = W

            # numeros aleatorios para os valores
            valores = np.random.randint(1, 200, n)

            # numeros aleatorios para os pesos
            pesos = np.random.randint(1, W, n)

            start = timeit.default_timer()
            resultadoEmPesos = fractionalKnapsack(valores, pesos, W)
            final = timeit.default_timer()

            time = final - start
            temposMochilaFracionaria.append(time)


            valorTotalNaMochila = 0

            for index, i in enumerate(resultadoEmPesos):
                valorTotalNaMochila += i * valores[index]

            table.at[linha, "n"] = n
            table.at[linha, "frac"] = round(valorTotalNaMochila, 2)
            table.at[linha, "tf"] = round(time, 12)

            linha = linha + 1
            n += 5
    print(table)
'''
 as linhas abaixos estão comentadas para gerar o gráfico.
 pegando a os n valores a partir de um W espeficico, como no ex do professor no pdf
'''
            # if(W == 20):
            #     testTabelaDeTempos.append(round(time, 12))
            #     testTableNitemsPorPeso.append(n)
            #     testTableResultadosSolFrac.append(round(resultadoEmValores, 2))
    # generateGraph(testTableNitemsPorPeso, testTableResultadosSolFrac)

