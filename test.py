import random
from ABR import *
from ARN import *
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.use("TkAgg")


def insertTest():
    minimumNodes = 100
    maximumNodes = 20000
    increment = 100

    numOfNodes = np.linspace(minimumNodes, maximumNodes, increment, dtype=int)
    insertABR = np.zeros(len(numOfNodes))
    insertARN = np.zeros(len(numOfNodes))

    for j in range(len(numOfNodes)):
        for i in range(50):
            nodes = np.arange(numOfNodes[j])
            np.random.shuffle(nodes)
            abr = ABR()
            arn = ARN()

            start = timer()
            for k in range(len(nodes)):
                abr.insert(nodes[k])
            end = timer()
            insertABRTime = end - start
            insertABR[j] += (insertABRTime)

            start = timer()
            for k in range(len(nodes)):
                arn.insert(nodes[k])
            end = timer()
            insertARNTime = end - start
            insertARN[j] += (insertARNTime)

    for k in range(len(insertABR)):
        insertABR[k] = ((insertABR[k] / 50) * 1000)
        insertARN[k] = ((insertARN[k] / 50) * 1000)

    plt.plot(numOfNodes.tolist(), insertABR.tolist(), label="Insert ABR Speed")
    plt.plot(numOfNodes.tolist(), insertARN.tolist(), label="Insert ARN Speed")
    plt.title("Confronto velocità inserimento")
    plt.legend(["ABR", "ARN"])
    plt.xlabel("Numero di Nodi")
    plt.ylabel("Tempo di Inserimento")
    # plt.show()
    plt.savefig("images/test_insert")
    plt.clf()
    plt.cla()


def createRandomABR(numOfNodes):
    nodes = [i for i in range(numOfNodes)]
    random.shuffle(nodes)
    abr = ABR()
    for i in range(len(nodes)):
        abr.insert(nodes[i])
    return abr


def createRandomARN(numOfNodes):
    nodes = [i for i in range(numOfNodes)]
    random.shuffle(nodes)
    arn = ARN()
    for i in range(len(nodes)):
        arn.insert(nodes[i])

    return arn


def searchTest():
    minimumNodes = 100
    maximumNodes = 20000
    increment = 100

    numOfNodes = np.linspace(minimumNodes, maximumNodes, increment, dtype=int)
    searchABR = np.zeros(len(numOfNodes))
    searchARN = np.zeros(len(numOfNodes))

    for j in range(len(numOfNodes)):
        for i in range(50):
            abr = createRandomABR(numOfNodes[j])
            arn = createRandomARN(numOfNodes[j])

            p = random.randint(0, numOfNodes[j])


            start = timer()
            abr.search(p)
            end = timer()
            searchABRTime = end - start
            searchABR[j] += searchABRTime

            start = timer()
            arn.search(p)
            end = timer()
            searchARNTime = end - start
            searchARN[j] += searchARNTime

    for k in range(len(numOfNodes)):
        searchABR[k] = ((searchABR[k] / 50) * 1000)
        searchARN[k] = ((searchARN[k] / 50) * 1000)

    plt.plot(numOfNodes, searchABR, label="Search ABR Speed")
    plt.plot(numOfNodes.tolist(), searchARN, label="Search ARN Speed")
    plt.title("Confronto velocità nella ricerca")
    plt.legend(["ABR", "ARN"])
    plt.xlabel("Numero di Nodi")
    plt.ylabel("Tempo in millisecondi")
    # plt.show()
    plt.savefig("images/test_search")

    plt.clf()
    plt.cla()


def heightTest():
    minimumNodes = 100
    maximumNodes = 20000
    increment = 100

    numOfNodes = np.linspace(minimumNodes, maximumNodes, increment, dtype=int)
    heightABR = np.zeros(len(numOfNodes))
    heightARN = np.zeros(len(numOfNodes))

    for j in range(len(numOfNodes)):
        for i in range(10):
            abr = createRandomABR(numOfNodes[j])
            arn = createRandomARN(numOfNodes[j])

            height = abr.getHeight()
            heightABR[j] += height

            height = arn.getHeight()
            heightARN[j] += height

    for k in range(len(numOfNodes)):
        heightABR[k] = (heightABR[k] / 10)
        heightARN[k] = (heightARN[k] / 10)

    plt.plot(numOfNodes, heightABR, label="ABR Height")
    plt.plot(numOfNodes, heightARN, label="ARN Height")
    plt.title("Confronto Altezze")
    plt.legend(["ABR", "ARN"])
    plt.xlabel("Numero di Nodi")
    plt.ylabel("Altezza albero")
    # plt.show()
    plt.savefig("images/test_height")
