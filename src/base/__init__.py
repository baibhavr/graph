from base.Graph import Graph

class initGraph:
    def __init__(self):
        self.g = Graph()
        
    def dummyGraph1(self):
        for i in range(10):
            self.g.addVertex(i)
            
        self.g.addEdge(1,2,2)
        self.g.addEdge(1,3,2)
        self.g.addEdge(2,4,5)
        self.g.addEdge(2,5,2)
        self.g.addEdge(3,6,1)
        self.g.addEdge(3,7,2)
        self.g.addEdge(5,8,2)
   
def main():        
    obj = initGraph()
    obj.dummyGraph1()
    obj.g.displayVertices()
    obj.g.displayEdges()

if __name__== "__main__":
    main()
    
