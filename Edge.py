import numpy as np
class Edge:
    def __init__(self,frm, to, functions, probaBadFunction) -> None:
        self.uuid = str(frm.uuid)+"-"+str(to.uuid)
        self.frm = frm
        self.to = to
        if isinstance(functions, dict):
            self.functions = functions
        elif isinstance(functions, list):
            self.functions = dict()
            for i in functions:
                self.functions[i] = self.genFunction(probaBadFunction)
        else:
            self.functions = {functions:self.genFunction(probaBadFunction)}

    def jsonFormat(self) -> str:
        return {
            "frm": self.frm.uuid,
            "to": self.to.uuid,
            "functions": self.functions,
        }
    
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
            p = round(np.random.uniform(1,10),2)
            form = f"lambda: np.random.choice([abs(np.random.chisquare({p})), -abs(np.random.chisquare({p/8})), -abs(np.random.chisquare({2*p}))],1,p=[{1-proba},{proba/2},{proba/2}])"
        return form

    def genVal(self) -> dict:
        out = dict()
        out["uuid"] = self.uuid
        out["val"] = dict()
        for i in self.functions:
            out["val"][i] = round(float(eval(self.functions[i])()), 3)
        out["from"] = self.frm.genVal()
        return out   

    def __str__(self) -> str:
        return str(self.uuid)