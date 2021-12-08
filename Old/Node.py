class Node:
    def __init__(self, id, functions, informations = None) -> None:
        self.id = id
        self.functions = functions
        self.informations = informations
        self.previous = []

    def addPrevious(self,edge) -> None:
        self.previous.append(edge)

    def genVal(self) -> dict:
        out = dict()
        for i in self.functions:
            out[i] = round(self.functions[i](),3)
        return out

    def __str__(self) -> str:
        a = str(self.id)+' | '
        for i in self.informations:
            a += str(i) + ' - ' + str(self.informations[i])+', ' 
        a = a[0:-2] + ' | '
        for i in self.functions:
            a += i + ', '
        a = a[0:-2]
        return a + ' | ' + str(list(map(lambda x: str(x.id),self.previous)))