from base.Vertex import Vertex  

'''
V = set of vertices
n = no. of vertices
'''

class Graph:
    def __init__(self):
        self.V = {}
        self.n = 0

    def addVertex(self,vid):
        self.n += 1
        new_v = Vertex(vid)
        self.V[vid] = new_v
        return new_v

    def getVertex(self,n):
        if n in self.V:
            return self.V[n]
        else:
            return None

    def addEdge(self,src,dest,weight=0):
        if src not in self.V:
            self.addVertex(src)
        if dest not in self.V:
            self.addVertex(dest)
        self.V[src].addNeighbor(self.V[dest], weight)

    def getVertices(self):
        return self.V.keys()
    
    def displayVertices(self):
        print("V =",list(self.V.keys()))
            
    def displayEdges(self):
        print("E = [")
        for src in self:
            for dest in src.getOutNeighbors():
                print((src.getId(), dest.getId(), src.getWeight(dest)))
        print("]")

    def __iter__(self):
        return iter(self.V.values())
    
g = Graph()
for i in range(10):
    g.addVertex(i)
    
g.addEdge(1,2,2)
g.addEdge(2,3,4)
g.addEdge(3,1,5)
g.addEdge(4,5,2)

g.displayVertices()
g.displayEdges()