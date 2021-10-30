from matplotlib import pyplot as plt

'''
script feito para plotar o gráfico automaticamente a partir dos valores gerados na tabela.
'''


def generateGraph(listaNitem , listX):


    # labels e title do gráfico definidos
    plt.xlabel('n')
    plt.title("Mochila")



    # plotando gráfico
    plt.plot(listaNitem, listX, label='Frac')


    plt.legend()

    plt.show()
