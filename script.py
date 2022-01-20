import numpy as np
import json
from Graph import Graph

# Init Graph
g = Graph()


# Generate
g.genGraph(15,3,["time","co2","water"],0.01)

# Store Graph as Json
#g.storeJson("data/Graph.json")

# # Load Graph from Json
# g.loadJson("Graph.json")
# print('Loaded')

# Display Graph networkx
#g.showGraph("images/graph.png")

# Generate Data
#data  = g.genData(100)
#print(data)

#Store Result As Json
# def storeJson(path) -> None:
#     with open(path, "w") as fp:
#         json.dump({'results':data}, fp)

# storeJson('data.json')

# Store Result as Neo4J
q = g.graphToNeo4J("bolt://localhost:7687","neo4j","pswd",False)
print(q)
q = g.dataToNeo4J(20,"bolt://localhost:7687","neo4j","pswd",False)
print(q)
# print(q[0]["extractId"])

# Todo

# Print Results
# print(data)

