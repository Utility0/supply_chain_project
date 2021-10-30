from Node import Node
import numpy as np

n = Node('Paris', (98723,91628), lambda x,y: np.random.normal(x,y))
print(n)