from numpy.random.mtrand import normal
from Edge import Edge
from Node import Node
import numpy as np
import json
import networkx as nx
import matplotlib.pyplot as plt
from neo4j import GraphDatabase

RAW = 1
TRANSFO = 2
HOUSEWARE = 3
SALES = 4

ranks = {}


class Graph:
    """A Supply Chain Graph generator"""
    def __init__(self, nodeDict={}, edgeDict={}) -> None:
        """Constructor
        
        Args:
            nodeDict (dict, optional): The node dictionary. Defaults to {}.
            edgeDict (dict, optional): The edge dictionary. Defaults to {}.
            
        Returns:
            None
        """

        self.nodeDict = nodeDict
        self.edgeDict = edgeDict

    def genGraph(self, size, couchesTransfo, functionsList, probaBadFunction):
        """
        Approximate Fibonacci sequence

        Args:
            n (int): The place in Fibonacci sequence to approximate

        Returns:
            float: The approximate value in Fibonacci sequence
        """

        prevLayer = []
        raw = []
        for _ in range(size): 
            idNewNode = self.genNode(RAW, functionsList, probaBadFunction) # Generate a new node
            ranks[idNewNode] = 0 # Set the rank of the node to 0
            prevLayer.append(idNewNode) # Add the node to the previous layer
            raw.append(idNewNode) # Add the node to the raw material layer

        ## GENERATE TRANSFORMATION LAYERS
        for l in range(1, couchesTransfo + 1): 
            tmp = []
            for _ in range(size*5): 
                idNewNode = self.genNode(TRANSFO, functionsList, probaBadFunction)
                ranks[idNewNode] = l
                fromNodes = np.random.choice(prevLayer, np.random.randint(2,5+1), replace=False)
                for i in fromNodes:
                    self.addEdge(self.nodeDict[i], self.nodeDict[idNewNode], functionsList, probaBadFunction)
                tmp.append(idNewNode)
            prevLayer += tmp
        transform = [i for i in prevLayer if i not in raw]
        # Gen Stockage Layer:
        stocks = []
        for _ in range(size*20):
            idNewNode = self.genNode(HOUSEWARE, functionsList, probaBadFunction)
            ranks[idNewNode] = couchesTransfo + 1
            fromNodes = np.random.choice(transform, np.random.randint(1,3+1), replace=False)
            for i in fromNodes:
                self.addEdge(self.nodeDict[i], self.nodeDict[idNewNode], functionsList, probaBadFunction)
            stocks.append(idNewNode)
        # Gen Sales Point Layer:
        salesPoints = []
        for _ in range(size*50):
            idNewNode = self.genNode(SALES, functionsList, probaBadFunction)
            ranks[idNewNode] = couchesTransfo+2
            fromNodes = np.random.choice(stocks, np.random.randint(1,5+1), replace=False)
            for i in fromNodes:
                self.addEdge(self.nodeDict[i], self.nodeDict[idNewNode], functionsList, probaBadFunction)
            salesPoints.append(idNewNode)

    def genNode(self,type,functionsList, probaBadFunction):
        """Generate a node
        
        Args:
            type (int): The type of the node.
            functionsList (list): The functions list.
            probaBadFunction (float): The probability of a bad function.
            
        Returns:
            Node: The generated node
        """

        n = Node(functionsList, probaBadFunction).setType(type)
        self.nodeDict[n.uuid] = n
        return n.uuid
    
    def addNode(self,node):
        """Adds a node to the graph
        
        Args:
            node (Node): The node to add.
            
        Returns:
            None
        """
        self.nodeDict[node.uuid] = node

    def addEdge(self, frm, to, functionsList, probaBadFunction):
        """Adds an edge to the graph
        
        Args:
            frm (Node): The node from which the edge is coming.
            to (Node): The node to which the edge is going.
            functionsList (list): The functions list.
            probaBadFunction (float): The probability of a bad function.
        
        Returns:
            None
        """

        edge = Edge(frm, to, functionsList, probaBadFunction)
        to.addPrevious(frm.uuid)
        frm.addNext(to.uuid)
        self.edgeDict[str(frm.uuid)+"-"+str(to.uuid)] = edge

    def recursiveWork(self,node) -> dict: 
        """Recursive work
        
        Args:
            node (Node): The node to work on.
            
        Returns:
            dict: The generated data
        """

        out = node.genVal()
        if node.type == RAW:
            return out
        else:
            out["from"] = list()
            for previous in node.previous:
                edge = self.edgeDict[previous+"-"+node.uuid]
                outEdge = edge.genVal()
                outEdge["from"] = self.recursiveWork(edge.frm)
                out["from"].append(outEdge)
            return out

    def genData(self,outputSize) -> list:
        """Generates the data of the graph
        
        Args:
            outputSize (int): The size of the output.
        
        Returns:
            list: The generated data
        """

        salespoints = [i for i in self.nodeDict.values() if i.type==SALES]
        salespoints = np.random.choice(salespoints, outputSize)
        out = list(map(self.recursiveWork, salespoints))
        return (out)

    def jsonFormat(self) -> str:
        """Generates the json format of the graph
        
        Returns:
            str: The generated json format
        """

        out = dict({"nodes":[],"edges":[]})
        for i in self.edgeDict:
            out["edges"].append(self.edgeDict[i].jsonFormat())
        for i in self.nodeDict:
            out["nodes"].append(self.nodeDict[i].jsonFormat())
        return out

    def storeJson(self,path) -> None:
        """Stores the json format of the graph
        
        Args:
            path (str): The path to store the json format.
            
        Returns:
            None"""

        with open(path, "w") as fp:
            json.dump(self.jsonFormat(), fp)

    def loadJson(self,file) -> None:
        """Loads the json format of the graph
        
        Args:
            file (str): The path to the json file.
            
        Returns:
            None
        """
        with open(file, "r") as f:
            data = json.load(f)
        nodes = data["nodes"]
        edges = data["edges"]
        for i in nodes:
            self.addNode(Node(
                {key: value for key, value in i["functions"].items()}, 
                    i["type"], 
                    i["uuid"],
                    i["previous"], 
                    i["next"], 
                    i["info"]))
        for i in edges:
            self.addEdge(self.nodeDict[i["frm"]], self.nodeDict[i["to"]], {key: value for key, value in i["functions"].items()},None)

    def showGraph(self,path) -> None:
        """Shows the graph 
        
        Args:
            path (str): The path to the json file.
            
        Returns:
            None
        """

        plt.figure(figsize=(16,9))
        nxG = nx.Graph()
        for i in list(self.nodeDict.values())[::-1]:
            nxG.add_node(i.uuid, subset=ranks[i.uuid])
        for i in list(self.edgeDict.values())[::-1]:
            nxG.add_edge(i.frm.uuid,i.to.uuid)

        color_map = []
        for idNode in nxG:
            node = self.nodeDict[idNode]
            if node.type == RAW:
                color_map.append('#1b85b8')
            elif node.type == TRANSFO:
                color_map.append('#f24457')
            elif node.type == HOUSEWARE:
                color_map.append('#fed95c')
            elif node.type == SALES:
                color_map.append('#90a0db')
            else:
                color_map.append('black')

        pos = nx.multipartite_layout(nxG) # Set horizontal layout
        nx.draw(nxG, pos, node_color=color_map, node_size=1000, alpha=0.8, with_labels=False, width=0.04, edge_color='black')
        plt.savefig(path, transparent=True) # Save plot to png
        plt.close()
    
    
    def toNeo4J(self,uri,name,password) -> str:
        """Save the supplyChain on neo4J
    
        Returns:
            bool: Succes of the export
        """
        #driver = GraphDatabase.driver(uri, auth=(name, password))
        for i in self.nodeDict:
            uuid=i
            print(self.nodeDict[i])
        querry="""
        create(n:Node{id:})
        """
        
           
        pass

    def __str__(self) -> str:
        """Generates the string representation of the graph
        
        Returns:
            str: The string representation of the graph
        """
        
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