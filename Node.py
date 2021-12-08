import uuid
import numpy as np

class Node:
    def __init__(self,functions, *arg) -> None:
        if len(arg) == 4:
            self.type = arg[0]
            self.uuid = arg[1]
            self.functions = functions
            self.previous = arg[2]     
            self.next = arg[3]
        else:
            if isinstance(functions,dict):
                self.functions = functions
            elif isinstance(functions,list):
                self.functions=dict()
                for i in functions:
                    self.functions[i]=self.genFunction()
            else:
                self.functions={functions:self.genFunction()}
            self.type = -1
            self.uuid= uuid.uuid1().hex
            self.previous = []
            self.next = []
    
    
    def genFunction(self) -> str:
        return 'lambda: np.random.uniform(9,99)'


    def addPrevious(self, prev):
        self.previous.append(prev)
        return self
    
    def addNext(self,next):
        self.next.append(next)
        return self

    def setType(self,type):
        self.type = type
        return self

    def jsonFormat(self) -> str:
        return {
            'type': self.type,
            'uuid': self.uuid,
            'functions': self.functions,
            'previous': self.previous,
            'next': self.next
        }
    
    def __str__(self) -> str:
        return str(self.uuid)+' '+str(self.type)+'\nPrevious : '+str(self.previous)+'\nNext : '+str(self.next)