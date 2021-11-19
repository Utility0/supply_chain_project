class Node:

    def __init__(self, id, location, randomFunction):
        self.id = id
        self.location = location
        self.randomFunction = randomFunction

    def fn(self,x):
        return self.randomFunction(*x)

    def __repr__(self) -> str:
        return str({'id': self.id, 'location': self.location, 'randomFunction': self.randomFunction})