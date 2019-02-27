class Vertex:
    def __init__(self,key):
        self.id = key
        self.outEdgeNeighbors = {}

    def addNeighbor(self,dest,weight=0):
        self.outEdgeNeighbors[dest] = weight

    def __str__(self):
        return str(self.id) + ' Out Edge Destinations: ' + str([x.id for x in self.outEdgeNeighbors])

    def getOutNeighbors(self):
        return self.outEdgeNeighbors.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.outEdgeNeighbors[nbr]