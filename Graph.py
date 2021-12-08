from Edge import Edge
from Node import Node
import numpy as np

RAW = 1
TRANSFO = 2
HOUSEWARE = 3
SALES = 4



import uuid

class Graph:
    def __init__(self, nodeDict={}, edgeList=[]) -> None:
        self.nodeDict = nodeDict
        self.edgeList = edgeList

    def genGraph(self, size, couchesTransfo):
        # Gen Raw Material Point
        
        prevLayer = []
        raw = []
        for _ in range(size):
            idNewNode = self.genNode(RAW)
            prevLayer.append(idNewNode)
            raw.append(idNewNode)
        # Gen Transformation Layer:
        for _ in range(couchesTransfo):
            tmp = []
            for _ in range(size*5):
                idNewNode = self.genNode(TRANSFO)
                fromNodes = np.random.choice(prevLayer,np.random.randint(2,5+1))
                for i in fromNodes:
                    self.addEdge(self.nodeDict[i],self.nodeDict[idNewNode])
                tmp.append(idNewNode)
            prevLayer += tmp
        transform = [i for i in prevLayer if i not in raw]
        # Gen Stockage Layer:
        stocks = []
        for _ in range(size*20):
            idNewNode = self.genNode(HOUSEWARE)
            fromNodes = np.random.choice(transform,np.random.randint(1,3+1))
            for i in fromNodes:
                self.addEdge(self.nodeDict[i],self.nodeDict[idNewNode])
            stocks.append(idNewNode)
        # Gen Sales Point Layer:
        salesPoints = []
        for _ in range(size*50):
            idNewNode = self.genNode(SALES)
            fromNodes = np.random.choice(stocks,np.random.randint(1,5+1))
            for i in fromNodes:
                self.addEdge(self.nodeDict[i],self.nodeDict[idNewNode])
            salesPoints.append(idNewNode)
        

                
    def genNode(self,type):
        n = Node().setType(type)
        self.nodeDict[n.uuid] = n
        return n.uuid

    def addEdge(self, frm,to):
        edge = Edge(frm,to,{'time' :lambda: np.random.uniform(0,1)})
        to.addPrevious(frm.uuid)
        frm.addNext(to.uuid)
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