class Edge:
    def __init__(self,id, frm, to, functions, informations = None) -> None:
        self.id =id
        self.frm = frm
        self.to = to
        self.functions = functions
        self.informations = informations
    
    def genVal(self) -> list:
        out = dict()
        for i in self.functions:
            out[i] = round(self.functions[i](),3)
        return out

    def __str__(self) -> str:
        a = str(self.id)+' | '+str(self.frm.id)+' --> '+str(self.to.id)+' | '
        for i in self.informations:
            a += str(i) + ' - ' + str(self.informations[i])+', '
        a = a[0:-2] + ' | '
        for i in self.functions:
            a += i + ', '
        return a[0:-2]