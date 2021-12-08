from Edge import Edge
from Node import Node
import numpy as np


import uuid
class Graph:
    def __init__(self, nodeDict={}, edgeList=[]) -> None:
        self.nodeDict = nodeDict
        self.edgeList = edgeList

    def genGraph(self, size, couchesTransfo):
        # Gen Raw Material Point
        raw = []
        for i in range(size):
            j = self.genNode()
            raw.append((j,False))
        # Gen Transfo



    def genNode(self):
        id = uuid.uuid1().hex
        self.nodeDict[id] = Node(id,{'time' :lambda: np.random.uniform(0,1)})
        return id

    def addEdge(self, frm,to,functions):
        edge = Edge(frm,to,functions)
        self.edgeList.append(edge)

    def __str__(self) -> str:
        a = "Graph :\n"
        a += "-"*20+"\n"
        a += "Nodes : "+"\n"
        for i in self.nodeDict:
            a += str(self.nodeDict[i])+"\n"
        a += "-"*20+"\n"
        a += "Edges : "+"\n"
        for i in self.edgeList:
            a += str(i)+"\n"
        a += "-"*20+"\n"
        return a


        return