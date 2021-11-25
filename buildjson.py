import json
import argparse


parser = argparse.ArgumentParser(description='Create example JSON for supply chain project', prog="Supply Chain Project")
parser.add_argument("-n","--numberOfNode", help="get the numbers of nodes for the JSON file, default=100", type = int, default=100)
args = parser.parse_args()

NUMBEROFNODE = args.numberOfNode
print(NUMBEROFNODE)