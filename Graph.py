from numpy.random.mtrand import normal
from Edge import Edge
from Node import Node
import numpy as np
import json
import networkx as nx
import matplotlib.pyplot as plt

RAW = 1
TRANSFO = 2
HOUSEWARE = 3
SALES = 4

ranks = {}


import uuid

class Graph:
    def __init__(self, nodeDict={}, edgeDict={}) -> None:
        self.nodeDict = nodeDict
        self.edgeDict = edgeDict

    def genGraph(self, size, couchesTransfo, functionsList, probaBadFunction):
        # Gen Raw Material Point
        prevLayer = []
        raw = []
        for _ in range(size):
            idNewNode = self.genNode(RAW,functionsList, probaBadFunction)
            ranks[idNewNode] = 0
            prevLayer.append(idNewNode)
            raw.append(idNewNode)
        # Gen Transformation Layer:
        for l in range(1,couchesTransfo+1):
            tmp = []
            for _ in range(size*5):
                idNewNode = self.genNode(TRANSFO,functionsList, probaBadFunction)
                ranks[idNewNode] = l
                fromNodes = np.random.choice(prevLayer,np.random.randint(2,5+1), replace=False)
                for i in fromNodes:
                    self.addEdge(self.nodeDict[i],self.nodeDict[idNewNode],functionsList, probaBadFunction)
                tmp.append(idNewNode)
            prevLayer += tmp
        transform = [i for i in prevLayer if i not in raw]
        # Gen Stockage Layer:
        stocks = []
        for _ in range(size*20):
            idNewNode = self.genNode(HOUSEWARE,functionsList, probaBadFunction)
            ranks[idNewNode] = couchesTransfo+1
            fromNodes = np.random.choice(transform,np.random.randint(1,3+1), replace=False)
            for i in fromNodes:
                self.addEdge(self.nodeDict[i],self.nodeDict[idNewNode],functionsList, probaBadFunction)
            stocks.append(idNewNode)
        # Gen Sales Point Layer:
        salesPoints = []
        for _ in range(size*50):
            idNewNode = self.genNode(SALES,functionsList, probaBadFunction)
            ranks[idNewNode] = couchesTransfo+2
            fromNodes = np.random.choice(stocks,np.random.randint(1,5+1), replace=False)
            for i in fromNodes:
                self.addEdge(self.nodeDict[i],self.nodeDict[idNewNode],functionsList, probaBadFunction)
            salesPoints.append(idNewNode)
        
 
 


    def genNode(self,type,functionsList, probaBadFunction):
        n = Node(functionsList, probaBadFunction).setType(type)
        self.nodeDict[n.uuid] = n
        return n.uuid
    
    def addNode(self,node):
        self.nodeDict[node.uuid] = node

    def addEdge(self, frm,to,functionsList, probaBadFunction):
        edge = Edge(frm,to,functionsList, probaBadFunction)
        to.addPrevious(frm.uuid)
        frm.addNext(to.uuid)
        self.edgeDict[str(frm.uuid)+"-"+str(to.uuid)] = edge

    def recurciveWork(self,node) -> dict: 
        out = node.genVal()
        if node.type == RAW:
            return out
        else:
            out["from"] = list()
            for previous in node.previous:
                edge = self.edgeDict[previous+"-"+node.uuid]
                outEdge = edge.genVal()
                outEdge["from"] = self.recurciveWork(edge.frm)
                out["from"].append(outEdge)
            return out


    def genData(self,outputSize) -> list:
        salespoints=[i for i in self.nodeDict.values() if i.type==SALES]
        salespoints =np.random.choice(salespoints,outputSize)
        out = list(map(self.recurciveWork,salespoints))
        return(out)

    def jsonFormat(self) -> str:
        out = dict({"nodes":[],"edges":[]})
        for i in self.edgeDict:
            out["edges"].append(self.edgeDict[i].jsonFormat())
        for i in self.nodeDict:
            out["nodes"].append(self.nodeDict[i].jsonFormat())
        return out

    def storeJson(self,path) -> None:
        with open(path, "w") as fp:
            json.dump(self.jsonFormat(), fp)

    def loadJson(self,file) -> None:
        with open(file, "r") as f:
            data = json.load(f)
        nodes = data["nodes"]
        edges = data["edges"]
        for i in nodes:
            self.addNode(Node({key: value for key, value in i["functions"].items()},i["type"],i["uuid"] ,i["previous"],i["next"], i["info"]))
        for i in edges:
            self.addEdge(self.nodeDict[i["frm"]], self.nodeDict[i["to"]],{key: value for key, value in i["functions"].items()},None)

    def showGraph(self,path) -> None:
        nxG = nx.DiGraph()
        for i in list(self.nodeDict.values())[::-1]:
            nxG.add_node(i.uuid, subset=ranks[i.uuid])
        for i in list(self.edgeDict.values())[::-1]:
            nxG.add_edge(i.frm.uuid,i.to.uuid)
        
        color_map = []
        for idNode in nxG:
            node = self.nodeDict[idNode]
            if node.type == RAW:
                color_map.append('blue')
            elif node.type == TRANSFO:
                color_map.append('green')
            elif node.type == HOUSEWARE:
                color_map.append('red')
            elif node.type == SALES:
                color_map.append('yellow')
            else:
                color_map.append('black')   
        pos = nx.multipartite_layout(nxG)  
        nx.draw(nxG, pos,node_color=color_map,node_size=100,alpha=.8, with_labels=False)
        plt.savefig("linear"+path)
        plt.close()



    def __str__(self) -> str:
        a = "Graph :\n"
        a += "-"*20+"\n"
        a += "Nodes : "+"\n"
        for i in self.nodeDict:
            a += str(self.nodeDict[i])+"\n"
        a += "-"*20+"\n"
        a += "Edges : "+"\n"
        for i in self.edgeDict:
            a += str(self.edgeDict[i])+"\n"
        a += "-"*20+"\n"
        return a

