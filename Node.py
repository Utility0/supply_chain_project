import uuid
import numpy as np

class Node:
    def __init__(self,functions, *arg) -> None:
        if len(arg) == 5:
            self.type = arg[0]
            self.uuid = arg[1]
            self.functions = functions
            self.previous = arg[2]     
            self.next = arg[3]
            self.info = arg[4]
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
            self.info = {}
    
    
    def genFunction(self) -> str:
        return "lambda: np.random.uniform(9,99)"


    def addPrevious(self, prev):
        self.previous.append(prev)
        return self
    
    def addNext(self,next):
        self.next.append(next)
        return self

    def setType(self,type):
        self.type = type
        return self

    def genVal(self) -> dict:
        out = dict()
        out["uuid"] = self.uuid
        out["val"]= dict()
        for i in self.functions:
            out["val"][i] = round(eval(self.functions[i])(),3)
        return out    

    def jsonFormat(self) -> str:
        return {
            "type": self.type,
            "uuid": self.uuid,
            "functions": self.functions,
            "previous": self.previous,
            "next": self.next,
            "info": self.info
        }
    
    def __str__(self) -> str:
        return str(self.uuid)+" "+str(self.type)+"\nPrevious : "+str(self.previous)+"\nNext : "+str(self.next)