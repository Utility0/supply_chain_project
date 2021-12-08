import json
import argparse

class RawMeterial:
    def __init__(self,id,used) -> None:
        self.id = id
        self.used = used


class Item:
    def __init__(self,id,childs=None) -> None:
        self.id = id
        self.childs = childs
    
    def isLinked(self) -> bool:
        if self.childs == None:
            return False
        else:
            return True

class Graph:
    def __init__(self) -> None:
        self.rawMaterials = {}
        self.items = {}



parser = argparse.ArgumentParser(description='Generate Random Supply Chain', prog="Supply Chain Project")
parser.add_argument("-ni","--numberItem", help="number of final items", type = int, required=True)
parser.add_argument("-nr","--numberRaw", help="number of raw materials", type = int, required=True)
args = parser.parse_args()

NUMBERRAW = args.numberRaw
NUMBERITEM = args.numberItem
G = Graph()

G.rawMaterials = dict(map(lambda x: ('r'+str(x),RawMeterial('r'+str(x),False)), range(NUMBERRAW)))
G.items = dict(map(lambda x: ('i'+str(x),Item('i'+str(x))), range(NUMBERITEM)))


print(G.rawMaterials)
print(G.finalItems)