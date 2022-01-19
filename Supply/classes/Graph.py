import numpy as np
import uuid
from numpy import random
from Edge import Edge
from Node import Node

import networkx as nx
import copy
import matplotlib.pyplot as plt

from Out import Out

RAW = 1
TRANSFO = 2
HOUSEWARE = 3
SALES = 4

class Graph:

    def __init__(self, nodeDict={}, edgeDict={}) -> None:
        self.nodeDict = nodeDict
        self.edgeDict = edgeDict
    
    def genGraph(self, size, couchesTransfo,functionsList ):
        if size <5:
            print("Minimum Number of Raw Meterial is 5")
            return False
        prevLayer = [] 
        raw = []

        ## Generate Raw Material Layer
        for _ in range(size): 
            idNewNode = self.genNode(RAW,0, functionsList) # Generate a new node
            prevLayer.append(idNewNode) # Add the node to the previous layer
            raw.append(idNewNode) # Add the node to the raw material layer

        ## GENERATE TRANSFORMATION LAYERS
        for l in range(1, couchesTransfo + 1): 
            tmp = []
            for _ in range(size*5): 
                idNewNode = self.genNode(TRANSFO,l, functionsList)
                fromNodes = np.random.choice(prevLayer, np.random.randint(2,5+1), replace=False)
                for i in fromNodes:
                    self.addEdge(i, idNewNode, functionsList )
                tmp.append(idNewNode)
            prevLayer += tmp
        transform = [i for i in prevLayer if i not in raw]
        # Gen Stockage Layer:
        stocks = []
        for _ in range(size*20):
            idNewNode = self.genNode(HOUSEWARE,couchesTransfo + 1, functionsList )
            fromNodes = np.random.choice(transform, np.random.randint(1,3+1), replace=False)
            for i in fromNodes:
                self.addEdge(i, idNewNode, functionsList )
            stocks.append(idNewNode)
        # Gen Sales Point Layer:
        salesPoints = []
        for _ in range(size*50):
            idNewNode = self.genNode(SALES,couchesTransfo+2, functionsList )
            fromNodes = np.random.choice(stocks, np.random.randint(1,5+1), replace=False)
            for i in fromNodes:
                self.addEdge(i, idNewNode, functionsList )
            salesPoints.append(idNewNode)
        self.salesPoints = salesPoints
        return True

    def genNode(self,type,rank,functionList):
        id = uuid.uuid1().hex
        functions = dict()
        for i in functionList:
            functions[i] = self.genFunctions()
        info = {'status':'unknown'}
        node = Node(id,type,rank,functions,info)
        self.nodeDict[id] = node
        return id


    def addEdge(self,frm,to,functionList):
        id = frm+'~'+to
        functions = dict()
        for i in functionList:
            functions[i] = self.genFunctions()
        info = {'status':'unknown'}
        edge = Edge(id,frm,to,functions,info)
        self.nodeDict[to].addPrevious(frm)
        self.edgeDict[id] = edge

    def genNData(self,numberFinalItem,wrong):
        for _ in range(numberFinalItem):
            graph = Graph({},{})
            node = np.random.choice(self.salesPoints,1)[0]
            self.genData(graph,node,wrong)
            return graph

    def genData(self,graph,nodeId,wrong):
        node = copy.copy(self.nodeDict[nodeId])
        node.genVal(wrong)
        graph.nodeDict[node.uuid] = node
        for i in node.previous:
            edge = copy.copy(self.edgeDict[i+"~"+nodeId])
            edge.genVal(wrong)
            graph.edgeDict[edge.uuid] = edge
            self.genData(graph,i,wrong)


    def genFunctions(self):
        return [lambda:1,lambda:2]


