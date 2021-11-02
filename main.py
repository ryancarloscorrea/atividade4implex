import math
import numpy as np
import pandas as pd
import timeit
from fractionalKnapsack import fractionalKnapsack
from binaryKnapsack import binaryKnapsack
from graph import generateGraph

'''
    primeira coluna da tabela é referente ao W
'''
if __name__ == '__main__':

    # testTabelaDeTemposFrac = []
    # testTableResultadosSolFrac = []
    #
    # testTableNitemsPorPeso = []
    #
    # testTabelaDeTemposBin = []
    # testTableResultadosSolBin = []

    linha = 0
    indexTable = []
    column = ["W", 'n', 'frac', 'bin','tf', 'tb']

    minW= int(input('Digite o valor minimo da capacidade da mochila:'))
    maxW = int(input('Digite o valor maximo da capacidade da mochila:'))
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
            valoresCopy = valores.copy()

            # numeros aleatorios para os pesos
            pesos = np.random.randint(1, W, n)
            pesosCopy = pesos.copy()

            # pegando tempo de execução do script fractionalKnapsack
            start = timeit.default_timer()
            resultadoEmPesos = fractionalKnapsack(valores, pesos, W)
            final = timeit.default_timer()

            timeFrac = final - start
            temposMochilaFracionaria.append(timeFrac)

            # pegando o valor total na mochila, com base no array retornado.

            valorTotalNaMochilaFrac = 0
            for index, i in enumerate(resultadoEmPesos):
                valorTotalNaMochilaFrac += i * valores[index]

            # pegando tempo de execução do script binaryKnapsack
            start = timeit.default_timer()
            matrizKbinary = binaryKnapsack(valoresCopy, pesosCopy, W)
            final = timeit.default_timer()

            timeBin = final - start

            # pegar o valor da mochila mais valiosa, linha abaixo corresponde a K[n][W]
            valorTotalBin = matrizKbinary[len(valoresCopy),W]


            '''
             preenchendo tabela nas linhas abaixo:
            '''
            table.at[linha, "n"] = n
            table.at[linha, "frac"] = round(valorTotalNaMochilaFrac, 2)
            table.at[linha, "bin"] = round(valorTotalBin)
            # table.at[linha, "w"] = valorEpeso[1]
            table.at[linha, "tf"] = round(timeFrac, 12)
            table.at[linha, "tb"] = round(timeBin, 12)

            linha = linha + 1
            # if(W == 50):
            #     testTabelaDeTemposFrac.append(round(timeFrac, 12))
            #     testTableResultadosSolFrac.append(round(valorTotalNaMochilaFrac, 2))
            #
            #     testTableNitemsPorPeso.append(n)
            #
            #     testTabelaDeTemposBin.append(round(timeBin, 12))
            #     testTableResultadosSolBin.append(round(valorTotalBin, 2))

            n += stepW
    # generateGraph(testTableNitemsPorPeso, testTabelaDeTemposFrac, testTabelaDeTemposBin)
    print(table)
'''
 as linhas abaixos estão comentadas para gerar o gráfico.
 pegando a os n valores a partir de um W espeficico, como no ex do professor no pdf
'''
