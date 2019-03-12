import queue as q

'''
BFS on a graph
If graph is weighted, ignores weights while traversing
'''
class BFS:
    def __init__(self,graph):
        self.graph = graph
        self.queue = q.Queue()
        self.visited = []

    def __str__(self):
        print("Traversal Sequence :",self.visited)
    
    def start(self,sourceId):
        self.source = self.graph.getVertex(sourceId)
        self.queue._put(self.source)
        
        '''ITERATE OVER THE QUEUE ITEMS'''
        while (self.queue.empty() is not True):
            current = self.queue.get()
            if(current.getId() not in self.visited):
                self.visited.append(current.getId())
                for neighbor in current.getOutNeighbors():
                    if(neighbor.getId() not in self.visited):
                        self.queue.put(neighbor)
    
#         print(self)
        print("Traversal Sequence :",self.visited)