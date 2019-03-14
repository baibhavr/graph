from base.Graph import Graph
from base import initGraph
from algorithms.SSSP import SSSP

def main():
    gObj = initGraph()
    gObj.dummyGraph1()
    g = gObj.g
    g.displayVertices()
    g.displayEdges()
    
    sssp = SSSP(g)
    sssp.Dijkstra(1)
    print(sssp)

if __name__== "__main__":
    main()