import uuid
import numpy as np
import random

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
                    self.functions[i]=self.genFunction(arg[0])
            else:
                self.functions={functions:self.genFunction(arg[0])}
            self.type = -1
            self.uuid= uuid.uuid1().hex
            self.previous = []
            self.next = []
            self.info = {}
    
    def genFunction(self, proba) -> str:
        UNIFORM = 1
        NORMAL = 2
        CHI = 3
        type = np.random.choice([UNIFORM,NORMAL,CHI],1)
        if type == UNIFORM:
            a = np.random.randint(1,90)
            b = np.random.randint(1,10)
            form = f"lambda: np.random.choice([abs(np.random.uniform({a},{a+b})),-abs(np.random.uniform({a+b},{a+2*b})),-abs(np.random.uniform({a-b},{a}))],1,p=[{1-proba},{proba/2},{proba/2}])"
        if type == NORMAL:
            µ = round(np.random.uniform(20,80),2)
            s = round(np.random.random()*5,2)
            form = f"lambda: np.random.choice([abs(np.random.normal({µ},{s})), -abs(np.random.normal({µ-5-4*s},{s/4})), -abs(np.random.normal({µ+5+4*s},{s/4}))],1,p=[{1-proba},{proba/2},{proba/2}])"
        if type == CHI:
            p =round(np.random.uniform(1,10),2)
            form = f"lambda: np.random.choice([abs(np.random.chisquare({p})), -abs(np.random.chisquare({p/8})), -abs(np.random.chisquare({2*p}))],1,p=[{1-proba},{proba/2},{proba/2}])"
        return form

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
            out["val"][i] = round(float(eval(self.functions[i])()),3)
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