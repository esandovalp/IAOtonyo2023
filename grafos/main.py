import networkx as nx
from Grafo import grafo
import matplotlib.pyplot as plt

G = grafo()

G.inserta('a','b',4)
G.inserta('a','h',8)
G.inserta('b','c',8)
G.inserta('b','h',11)
G.inserta('h','i',7)
G.inserta('h','g',1)
G.inserta('i','c',2)
G.inserta('i','g',6)
G.inserta('c','f',4)
G.inserta('c','d',7)
G.inserta('g','f',2)
G.inserta('d','e',9)
G.inserta('d','f',14)
G.inserta('f','e',10)

print('DFS traversal:\n',G.DFS(),'\n')
print('Prim:\n',G.Prim(),'\n')
print('BFS traversal:\n',G.BFS('a'),'\n')
gr1 = nx.Graph(G.G)
nx.draw(gr1,with_labels=True)
plt.show()