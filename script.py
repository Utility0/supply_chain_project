import numpy as np
import cmd
import argparse
from Graph import Graph
from Edge import Edge
from Node import Node

# Init Graph
g = Graph()


# Generate
g.genGraph(5,2,['time','co2'])

print(g.jsonFormat())

print(g)
