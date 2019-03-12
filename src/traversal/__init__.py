from base.Graph import Graph
from traversal.BFS import BFS
import base
from base import initGraph

def main():
    gObj = initGraph()
    gObj.dummyGraph1()
    g = gObj.g
    g.displayVertices()
    g.displayEdges()
    
    bfs = BFS(g)
    bfs.start(1)
    
  
if __name__== "__main__":
    main()