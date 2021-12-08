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

    def genGraph(self, size, couchesTransfo, functionsList):
        # Gen Raw Material Point
        
        prevLayer = []
        raw = []
        for _ in range(size):
            idNewNode = self.genNode(RAW,functionsList)
            prevLayer.append(idNewNode)
            raw.append(idNewNode)
        # Gen Transformation Layer:
        for _ in range(couchesTransfo):
            tmp = []
            for _ in range(size*5):
                idNewNode = self.genNode(TRANSFO,functionsList)
                fromNodes = np.random.choice(prevLayer,np.random.randint(2,5+1), replace=False)
                for i in fromNodes:
                    self.addEdge(self.nodeDict[i],self.nodeDict[idNewNode],functionsList)
                tmp.append(idNewNode)
            prevLayer += tmp
        transform = [i for i in prevLayer if i not in raw]
        # Gen Stockage Layer:
        stocks = []
        for _ in range(size*20):
            idNewNode = self.genNode(HOUSEWARE,functionsList)
            fromNodes = np.random.choice(transform,np.random.randint(1,3+1), replace=False)
            for i in fromNodes:
                self.addEdge(self.nodeDict[i],self.nodeDict[idNewNode],functionsList)
            stocks.append(idNewNode)
        # Gen Sales Point Layer:
        salesPoints = []
        for _ in range(size*50):
            idNewNode = self.genNode(SALES,functionsList)
            fromNodes = np.random.choice(stocks,np.random.randint(1,5+1), replace=False)
            for i in fromNodes:
                self.addEdge(self.nodeDict[i],self.nodeDict[idNewNode],functionsList)
            salesPoints.append(idNewNode)
        

                
    def genNode(self,type,functionsList):
        n = Node(functionsList).setType(type)
        self.nodeDict[n.uuid] = n
        return n.uuid

    def addEdge(self, frm,to,functionsList):
        edge = Edge(frm,to,functionsList)
        to.addPrevious(frm.uuid)
        frm.addNext(to.uuid)
        self.edgeList.append(edge)

    def jsonFormat(self) -> str:
        out = dict({'nodes':[],'edges':[]})
        for i in self.edgeList:
            out['edges'].append(i.jsonFormat())
        for i in self.nodeDict:
            out['nodes'].append(self.nodeDict[i].jsonFormat())
        return out

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