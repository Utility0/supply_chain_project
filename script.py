import numpy as np
import json
from Graph import Graph

# Init Graph
g = Graph()


# Generate
g.genGraph(15,3,["time","co2"],0.01)

# Store Graph as Json
g.storeJson("Graph.json")

# # Load Graph from Json
# g.loadJson("Graph.json")
# print('Loaded')

# Display Graph networkx
#g.showGraph("graph.png")

# Generate Data
data  = g.genData(100)
print('Gen')

#Store Result As Json
def storeJson(path) -> None:
    with open(path, "w") as fp:
        json.dump({'results':data}, fp)

storeJson('data.json')

# Store Result as Neo4J
#
#
# Todo

# Print Results
# print(data)

