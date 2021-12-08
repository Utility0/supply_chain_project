class Node:
    def __init__(self,id, functions) -> None:
        self.id = id
        self.functions = functions

    def __str__(self) -> str:
        return str(self.id)