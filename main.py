from Node import Node
import numpy as np

strnormal = 'lambda x,y : np.random.normal(x,y)'

normal= eval(strnormal)

print(normal(3,7))

# def normal(x,y):
#     return np.random.normal(x,y)

# n = Node('Paris', (98723,91628), normal)
# print(n.fn((3,7)))
# print(n.fn((3,7)))
# print(n.fn((3,7)))
# normal(2,3)