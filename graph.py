from matplotlib import pyplot as plt

'''
script feito para plotar o gráfico automaticamente a partir dos valores gerados na tabela.
'''


def generateGraph(listaNitem , listXFrac, listXbin):


    # labels e title do gráfico definidos
    plt.xlabel('n')
    plt.title("Mochila")



    # plotando gráfico
    plt.plot(listaNitem, listXFrac, label='Frac')
    plt.plot(listaNitem, listXbin, label='Bin')


    plt.legend()

    plt.show()
