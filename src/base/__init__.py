from base.Graph import Graph

class initGraph:
    def __init__(self):
        self.g = Graph()
        
    def dummyGraph(self):
        for i in range(10):
            self.g.addVertex(i)
            
        self.g.addEdge(1,2,2)
        self.g.addEdge(2,3,4)
        self.g.addEdge(3,1,5)
        self.g.addEdge(4,5,2)
        
        
def main():        
    obj = initGraph()
    obj.dummyGraph()
    obj.g.displayVertices()
    obj.g.displayEdges()

if __name__== "__main__":
    main()
    
