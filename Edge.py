class Edge:
    def __init__(self,frm, to, functions) -> None:
        self.uuid = str(frm.uuid)+'-'+str(to.uuid)
        self.frm = frm
        self.to = to

    def __str__(self) -> str:
        return str(self.uuid)