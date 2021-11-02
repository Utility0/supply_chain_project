import numpy as np
from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = defaultdict(lambda:[])
        self.edges = defaultdict(lambda:[])

class Node:
    def __init__(self, randomFunction):
        self.randomFunction = randomFunction


class Edge:
    def __init__(self, fr, to, features):
        self.fr = fr
        self.to = to
        self.features = features

g= Graph()

g.addNode('paris', lambda x,y:np.random.uniform(x,y))
g.addNode('marseille', lambda x,y: np.random.uniform(x,y))
g.addNode('lyon', lambda x,y:np.random.uniform(x,y))
g.addEdge('marseille', 'paris',0)
print(g.getNodes())
print(g.getEdges())
print('-'*10)
g.removeNode('paris')
print(g.getNodes())
print(g.getEdges())
print('-'*10)