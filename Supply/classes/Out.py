from Graph import Graph
import networkx as nx
import matplotlib.pyplot as plt
class Out:
    def __init__(self) -> None:
        pass

    def nxplot(graph,path):
        nxG = nx.DiGraph()
        for i in list(graph.nodeDict.values()):
            nxG.add_node(i.uuid)
        for i in list(graph.edgeDict.values()):
            nxG.add_edge(i.frm,i.to)
        nx.draw(nxG)
        plt.savefig(path, transparent=False) # Save plot to png
        plt.close()
