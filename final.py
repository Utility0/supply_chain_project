import numpy as np
import json
import re
from Node import Node
from Edge import Edge
from Graph import Graph


g = Graph()
g.loadJson('data.json')
print(g)
print(g.recurciveWork('n3'))