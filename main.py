from Node import Node
import numpy as np

normal = lambda x,y: np.random.normal(x,y)

n = Node('Paris', (98723,91628), normal)
print(n)