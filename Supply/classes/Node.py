import inspect
import random

class Node:
    def __init__(self,uuid,type,rank,functions,info) -> None:
        self.uuid = uuid
        self.type = type
        self.rank = rank
        self.functions = functions
        self.info = info
        self.val = None
        self.previous = []
    
    def genVal(self,wrong):
        self.val = dict()
        for i in self.functions:
            if random.uniform(0,1) > wrong:
                self.val[i] = (True,self.functions[i][0]())
            else:
                self.val[i] = (False,self.functions[i][1]())
        return True

    def JsonFormat(self):
        return {
            'uuid':self.uuid,
            'type':self.type,
            'functions':self.functions,
            'info':self.info
        }
    def addPrevious(self,idPrevious):
        self.previous.append(idPrevious)
        