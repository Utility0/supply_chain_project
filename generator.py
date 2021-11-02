import numpy as np
import math
# Nombre de site d'extraction de matière première
MATIERE_PREMIERE = 500
RAW_MATERIAL = 1

nodes = [(i,0, RAW_MATERIAL) for i in range(MATIERE_PREMIERE)]
edges = []


def generateLayer(nodes, edges):
    maxLayer = max(list(map(lambda x: x[1], nodes)))
    newLayer = maxLayer+1
    effectiveLayer = [i for i in range(maxLayer-2,maxLayer+1) if i >= 0]
    numberNodesLayer = list(map(lambda x: len([i for i in nodes if i[1]==x]),effectiveLayer))
    if(len(numberNodesLayer) == 1):
        newLayerNumber = math.floor(np.dot(np.asarray(numberNodesLayer), np.asarray([0.50])))   
    elif(len(numberNodesLayer) == 2):
        newLayerNumber = math.floor(np.dot(np.asarray(numberNodesLayer), np.asarray([0.3, 0.50])))   
    else:
        newLayerNumber = math.floor(np.dot(np.asarray(numberNodesLayer), np.asarray([0.1, 0.3, 0.50])))
    for i in range(newLayerNumber):
        nodes.append((i,newLayer,RAW_MATERIAL))
    if newLayerNumber==0:
        return True
    return False


a = False
i = 0
while not a:
    a = generateLayer(nodes, edges)
    print(i)
    i+=1

print(nodes)
print(list(map(lambda x: len([i for i in nodes if i[1]==x]), list(set(map(lambda x: x[1], nodes))))))
print(len(nodes))