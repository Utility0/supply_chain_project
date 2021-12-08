import argparse as arg
import random as rand
import numpy as np

parser = arg.ArgumentParser(description='Process some integers.')
parser.add_argument('range', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('step', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
args = parser.parse_args()

functions = []
ran = int(args.range[0])
step = int(args.step[0])
for i in range(10, ran, step):
    for j in range(1, 10):
        functions.append(f"lambda: abs(np.random.uniform({rand.randint(0,i)},{i}))")
        functions.append(f"lambda: abs(np.random.poisson({rand.randint(0,i)}))")
        functions.append(f"lambda: abs(np.random.normal({rand.randint(0,i)}))")
    
with open("functions.txt", "w") as f:
    for i in functions:
        f.write(f"{i}\n")
