from base.Graph import Graph
from traversal.BFS import BFS
import base
from base import initGraph

def main():
    gObj = initGraph()
    gObj.dummyGraph()
    g = gObj.g
    g.displayVertices()
    g.displayEdges()
    
    bfs = BFS(g)
    bfs.start(8)
    
  
if __name__== "__main__":
    main()