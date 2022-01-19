from numpy import random


import random
class Edge:
    def __init__(self,uuid,frm,to,functions,info) -> None:
        self.uuid = uuid
        self.frm = frm
        self.to = to
        self.functions = functions
        self.info = info
        self.val = None

    def genVal(self,wrong):
        self.val = dict()
        for i in self.functions:
            if random.uniform(0,1) > wrong:
                self.val[i] = (True,self.functions[i][0]())
            else:
                self.val[i] = (False,self.functions[i][1]())
        return True

    def JsonFormat(self):
        out = {
            'uuid':self.uuid,
            'frm':self.frm,
            'to':self.to,
            'functions':self.functions,
            'info':self.info
        }


        