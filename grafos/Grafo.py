import heapdict as hd
import numpy as np


class grafo:
    def __init__(self):
        self.G = {}

    def insertaD(self, v1, v2, w=0):
        if v1 not in self.G:
            self.G[v1] = {}
        self.G[v1][v2] = w
        if v2 not in self.G:
            self.G[v2] = {}

    def inserta(self, v1, v2, w=0):
        self.insertaD(v1, v2, w)
        self.insertaD(v2, v1, w)

    def __DFS(self, actual, visitados, lista):
        if visitados[actual]:
            return
        visitados[actual] = True
        lista += [actual]
        for vecino in self.G[actual]:
            self.__DFS(vecino, visitados, lista)

    def DFS(self):
        visitados = {}
        for i in self.G:
            visitados[i] = False
        lista = []
        for i in visitados:
            if not visitados[i]:
                self.__DFS(i, visitados, lista)
        return lista

    def BFS(self, inicio):
        Q = [inicio]
        G = self.G
        lista = []
        # inicializa visitados
        visitados = {}
        for i in self.G:
            visitados[i] = False
        while len(Q) > 0:
            actual = Q.pop()
            visitados[actual] = True
            lista += actual
            for v in G[actual]:
                if not visitados[v]:
                    Q.append(v)
        return lista

    def _prim(self, inicial):
        papa = {}
        valor = {}
        Q = hd.heapdict()
        for i in self.G:
            valor[i] = np.inf
            papa[i] = None
            Q[i] = np.inf
        Q[inicial] = 0
        while len(Q) > 0:
            v1, peso = Q.popitem()
            for vecino in self.G[v1]:
                if vecino in Q and self.G[v1][vecino] < valor[vecino]:
                    valor[vecino] = self.G[v1][vecino]
                    Q[vecino] = self.G[v1][vecino]
                    papa[vecino] = v1
        return papa

    def Prim(self):
        if len(self.G.keys()) == 0:
            return
        return self._prim(list(self.G.keys())[0])
