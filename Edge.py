class Edge:
    def __init__(self,frm, to, functions) -> None:
        self.id = str(frm.id)+'-'+str(to.id)
        self.frm = frm
        self.to = to

    def __str__(self) -> str:
        return str(self.id)