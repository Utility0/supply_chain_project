import numpy as np
from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = defaultdict(lambda:[])
        self.edges = defaultdict(lambda:[])

    def addNode(self, id,randomFunction):
        self.nodes[id] = Node(randomFunction)

    def addEdge(self, fr,to,feature):
        if (fr in self.nodes) and (to in self.nodes):
            self.edges[fr].append(Edge(fr,to,feature)) 

    def removeEdge(self, fr, to):
        if (fr in self.nodes) and (to in self.nodes):
            for i in self.edges[fr]:
                if i.to == to:
                    self.edges[fr].remove(i)

    def removeNode(self, id):
        self.nodes.pop(id)
        if id in self.edges:
            self.edges.pop(id)
        l = list(self.edges)
        for i in l:
            for j in self.edges[i]:
                if j.to == id:
                    if len(self.edges[i]) == 1:
                        self.edges.pop(i)
                    else:
                        self.edges[i].remove(j)

            

    def getNodes(self):
        return self.nodes
    
    def getEdges(self):
        return self.edges

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