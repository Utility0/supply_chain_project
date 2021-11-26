import json
import argparse
from Node import Node
from Edge import Edge
from Graph import Graph


parser = argparse.ArgumentParser(description='Create example JSON for supply chain project', prog="Supply Chain Project")
parser.add_argument("-f","--file", help="path to the JSON file", type = str, required=True)
args = parser.parse_args()

FILEPATH = args.file

g = Graph()
g.loadJson(FILEPATH)
print(g)
print(g.recurciveWork('n3'))