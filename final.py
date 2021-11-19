import numpy as np
import json
import re



class Node:
    def __init__(self, id, functions, informations = None) -> None:
        self.id = id
        self.functions = functions
        self.informations = informations
        self.previous = []

    def addPrevious(self,edge) -> None:
        self.previous.append(edge)

    def genVal(self) -> dict:
        out = dict()
        for i in self.functions:
            out[i] = round(self.functions[i](),3)
        return out

    def __str__(self) -> str:
        a = str(self.id)+' | '
        for i in self.informations:
            a += str(i) + ' - ' + str(self.informations[i])+', ' 
        a = a[0:-2] + ' | '
        for i in self.functions:
            a += i + ', '
        a = a[0:-2]
        return a + ' | ' + str(list(map(lambda x: str(x.id),self.previous)))
class Edge:
    def __init__(self,id, frm, to, functions, informations = None) -> None:
        self.id =id
        self.frm = frm
        self.to = to
        self.functions = functions
        self.informations = informations
    
    def genVal(self) -> list:
        out = dict()
        for i in self.functions:
            out[i] = round(self.functions[i](),3)
        return out

    def __str__(self) -> str:
        a = str(self.id)+' | '+str(self.frm.id)+' --> '+str(self.to.id)+' | '
        for i in self.informations:
            a += str(i) + ' - ' + str(self.informations[i])+', '
        a = a[0:-2] + ' | '
        for i in self.functions:
            a += i + ', '
        return a[0:-2]
class Graph:
    def __init__(self) -> None:
        self.nodeList = {}
        self.edgeList = []

    def addNode(self,node) -> None:
        id = node.id
        self.nodeList[id] = node

    def addEdge(self,edge) -> None:
        self.edgeList.append(edge)
        self.nodeList[edge.to.id].addPrevious(edge)



    def loadJson(self,file) -> None:
        with open(file, 'r') as f:
            data = json.load(f)
        nodes = data['nodes']
        edges = data['edges']
        for i in nodes:
            self.addNode(Node(i['id'], {key: eval(value) for key, value in i['functions'].items()}, i['informations']))
        for i in edges:
            self.addEdge(Edge(i['id'], self.nodeList[i['frm']], self.nodeList[i['to']],{key: eval(value) for key, value in i['functions'].items()}, i['informations']))

    def workNode(self,nodeId) -> dict:
        return self.nodeList[nodeId].genVal()

    def recurciveWork(self,nodeId) -> dict: 
        if len(self.nodeList[nodeId].previous) == 0:
            return {'nodeId':nodeId, 'values': self.workNode(nodeId)}
        else:
            out = {'nodeId':nodeId, 'values': self.workNode(nodeId), 'from' : []}
            for edge in self.nodeList[nodeId].previous:
                out['from'].append({'edgeId': edge.id, 'values':edge.genVal(), 'previous': self.recurciveWork(edge.frm.id)})
            return out

    def __str__(self) -> str:
        a = "Graph :\n"
        a += "-"*20+"\n"
        a += "Nodes : "+"\n"
        for i in self.nodeList:
            a += str(self.nodeList[i])+"\n"
        a += "-"*20+"\n"
        a += "Edges : "+"\n"
        for i in self.edgeList:
            a += str(i)+"\n"
        a += "-"*20+"\n"
        return a

g = Graph()
g.loadJson('data.json')
print(g)
print(g.recurciveWork('n3'))