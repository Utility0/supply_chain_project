from classes.Graph import Graph
from classes.Out import Out

g = Graph()
g.genGraph(5,1,["time","co2"])


generatedGraph = g.genNData(1,0.001)

Out().nxplot(g,"out.png")