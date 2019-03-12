from base.Graph import Graph
from traversal.Traverse import Traverse
import base
from base import initGraph

def main():
    gObj = initGraph()
    gObj.dummyGraph1()
    g = gObj.g
    g.displayVertices()
    g.displayEdges()
    
    t = Traverse(g)
    print("DFS traversal :",t.startDFS(1))
    print("BFS traversal :",t.startBFS(1))
  
if __name__== "__main__":
    main()