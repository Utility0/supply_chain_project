#----------------------------------------------#
#         Import Packages
#----------------------------------------------#
import json
import argparse
import numpy as np
from Node import Node

#----------------------------------------------#
#         Import Variables
#----------------------------------------------#

parser = argparse.ArgumentParser(description='Create example JSON for supply chain project', prog="Supply Chain Project")
parser.add_argument("-n","--numberOfNode", help="get the numbers of nodes for the JSON file", type = int, required=True)
parser.add_argument("-f","--functions", nargs="+", help="get the names of the functions", type = str, required=True)
args = parser.parse_args()

#----------------------------------------------#
#         Set Variables
#----------------------------------------------#

NUMBEROFNODE = args.numberOfNode
FUNCTIONSNAMES = args.functions
NumberOfFunctions = len(FUNCTIONSNAMES)


#----------------------------------------------#
#         Create The Ids
# Input:  Number of Nodes
# Output: list nodes id
#----------------------------------------------#
size = len(str(NUMBEROFNODE))
def addZeros(str):
    while(len(str)) != size:
        str= '0'+str
    return str
ids = [str(i+1) for i in range(NUMBEROFNODE)]
ids = list(map(addZeros,ids))
# List of Nodes ids

#----------------------------------------------#
#         Create The Functions
# Input:  list nodes id
# Output: dict nodes id: dict functions
#----------------------------------------------#
def addFunctions(ids):
    out = {i:{} for i in ids}
    for i in out:
        for j in FUNCTIONSNAMES:
            pass




#n = Node()