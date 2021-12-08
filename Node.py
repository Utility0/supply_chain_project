import uuid
import numpy as np

class Node:
    def __init__(self, *arg) -> None:
        if len(arg) == 5:
            self.type = arg[0]
            self.uuid = arg[1]
            self.functions = arg[2]
            self.previous = arg[3]     
            self.next = arg[4]
        else:
            self.type = -1
            self.uuid= uuid.uuid1().hex
            self.functions = {'time' :lambda: np.random.uniform(0,1)}
            self.previous = []
            self.next = []

    def addPrevious(self, prev):
        self.previous.append(prev)
        return self
    
    def addNext(self,next):
        self.next.append(next)
        return self

    def setType(self,type):
        self.type = type
        return self
    def __str__(self) -> str:
        return str(self.uuid)+' '+str(self.type)+'\nPrevious : '+str(self.previous)+'\nNext : '+str(self.next)