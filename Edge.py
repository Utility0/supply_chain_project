import numpy as np
class Edge:
    def __init__(self,frm, to, functions) -> None:
        self.uuid = str(frm.uuid)+"-"+str(to.uuid)
        self.frm = frm
        self.to = to
        if isinstance(functions,dict):
            self.functions = functions
        elif isinstance(functions,list):
            self.functions=dict()
            for i in functions:
                self.functions[i]=self.genFunction()
        else:
            self.functions={functions:self.genFunction()}


    def jsonFormat(self) -> str:
        return {
            "frm": self.frm.uuid,
            "to": self.to.uuid,
            "functions": self.functions,
        }

    
    def genFunction(self) -> str:
        return "lambda: np.random.uniform(9,99)"

    def genVal(self) -> dict:
        out = dict()
        out["uuid"] = self.uuid
        out["val"]= dict()
        for i in self.functions:
            out["val"][i] = round(eval(self.functions[i])(),3)
        out["from"] = self.frm.genVal()
        return out   

    def __str__(self) -> str:
        return str(self.uuid)